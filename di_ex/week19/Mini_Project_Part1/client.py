import asyncio
import os
import json
import signal
import psutil
from typing import List, Dict, Any
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from contextlib import AsyncExitStack
from groq import AsyncGroq

load_dotenv()


class StandaloneMCPAgent:
    def __init__(self):
        self.groq = AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))
        self.exit_stack = AsyncExitStack()
        self.sessions: Dict[str, ClientSession] = {}
        self.tools_metadata = []
        self.processes = []

    async def connect_server(self, name: str, command: str, args: List[str]):
        """Connects to a server and adds ONLY essential tools to save tokens."""
        print(f"📡 Connecting to {name} server...")

        clean_env = os.environ.copy()
        clean_env["PYTHONUNBUFFERED"] = "1"

        server_params = StdioServerParameters(command=command, args=args, env=clean_env)

        read, write = await self.exit_stack.enter_async_context(
            stdio_client(server_params)
        )
        session = await self.exit_stack.enter_async_context(ClientSession(read, write))

        await session.initialize()
        self.sessions[name] = session

        # Pull tools from the server
        tools_resp = await session.list_tools()

        # --- TOKEN OPTIMIZATION START ---
        # Define which tools we actually need for the exercise
        essential_tools = {
            "github": ["search_repositories", "get_repository", "get_user"],
            "brave": ["brave_web_search"],
        }

        count = 0
        for tool in tools_resp.tools:
            # Only add the tool if it's in our essential list
            if tool.name in essential_tools.get(name, []):
                self.tools_metadata.append(
                    {
                        "name": tool.name,
                        "server": name,
                        "definition": {
                            "name": tool.name,
                            "description": tool.description[
                                :150
                            ],  # Trim long descriptions
                            "parameters": tool.inputSchema,
                        },
                    }
                )
                count += 1
        # --- TOKEN OPTIMIZATION END ---

        print(f"✅ {name} connected (using {count}/{len(tools_resp.tools)} tools).")

    async def call_llm(self, messages: List[dict]):
        # Proper wrapping for Groq/OpenAI tool format
        formatted_tools = [
            {
                "type": "function",
                "function": t[
                    "definition"
                ],  # This is the actual schema from the MCP server
            }
            for t in self.tools_metadata
        ]

        return await self.groq.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            tools=formatted_tools,  # Use the wrapped tools
            tool_choice="auto",
        )

    async def chat(self, user_prompt: str):
        print(f"\n💬 User: {user_prompt}")
        messages = [{"role": "user", "content": user_prompt}]

        # Agentic Loop (Max 5 steps to prevent infinite loops)
        for _ in range(5):
            response = await self.call_llm(messages)
            assistant_msg = response.choices[0].message
            messages.append(assistant_msg)

            if not assistant_msg.tool_calls:
                return assistant_msg.content

            # Handle Tool Calls
            for tool_call in assistant_msg.tool_calls:
                tool_name = tool_call.function.name
                tool_args = json.loads(tool_call.function.arguments)

                # Find which server owns this tool
                meta = next(t for t in self.tools_metadata if t["name"] == tool_name)
                session = self.sessions[meta["server"]]

                print(f"🛠️  Calling {tool_name} on {meta['server']}...")
                result = await session.call_tool(tool_name, tool_args)

                # Add result to conversation
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "name": tool_name,
                        "content": str(result.content),
                    }
                )

    async def stop(self):
        await self.exit_stack.aclose()
        print("🔌 All servers shut down.")


async def main():
    agent = StandaloneMCPAgent()
    try:
        # Connect to existing servers (Part 1)
        # Ensure NVM is set up so 'npx' is in your path!
        await agent.connect_server(
            "github", "npx", ["-y", "@modelcontextprotocol/server-github"]
        )
        await agent.connect_server(
            "brave", "npx", ["-y", "@modelcontextprotocol/server-brave-search"]
        )

        # Run the test prompt
        prompt = "Find the GitHub profile for 'hynek' and search the web for his most recent 2025 conference talks."
        final_answer = await agent.chat(prompt)
        print(f"\n✨ FINAL REPORT:\n{final_answer}")

    finally:
        await agent.stop()


if __name__ == "__main__":
    asyncio.run(main())
