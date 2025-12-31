import os
import json
import asyncio
from typing import List, Dict
from groq import AsyncGroq
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from contextlib import AsyncExitStack


class LeanMCPAgent:
    def __init__(self):
        # Initialize Groq Client
        self.groq = AsyncGroq(api_key=os.environ.get("GROQ_API_KEY"))
        self.exit_stack = AsyncExitStack()

        # Dictionary to map tool names to specific server sessions
        # Format: {"tool_name": session_object}
        self.tool_map: Dict[str, ClientSession] = {}
        self.sessions: List[ClientSession] = []

    async def connect_server(self, name: str, command: str, args: List[str]):
        """Connects to an MCP server and indexes its tools."""
        print(f"📡 Connecting to {name}...")

        server_params = StdioServerParameters(
            command=command, args=args, env=os.environ.copy(), shell=True
        )

        # Establish connection
        stdio_transport = await self.exit_stack.enter_async_context(
            stdio_client(server_params)
        )
        read, write = stdio_transport
        session = await self.exit_stack.enter_async_context(ClientSession(read, write))

        await session.initialize()
        self.sessions.append(session)

        # Map tools to this session so we know who to call later
        tool_resp = await session.list_tools()
        for tool in tool_resp.tools:
            self.tool_map[tool.name] = session

        print(f"✅ {name} connected with {len(tool_resp.tools)} tools.")

    async def get_all_tools_formatted(self):
        """Returns all tools from all servers in Groq/OpenAI format."""
        all_tools = []
        for session in self.sessions:
            tool_resp = await session.list_tools()
            for t in tool_resp.tools:
                all_tools.append(
                    {
                        "type": "function",
                        "function": {
                            "name": t.name,
                            "description": t.description or f"Use tool {t.name}",
                            "parameters": t.inputSchema,
                        },
                    }
                )
        return all_tools

    async def chat(self, prompt: str):
        """The main execution loop (supports multi-step planning)."""
        tools = await self.get_all_tools_formatted()
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant with access to local notes, GitHub, and Brave Search. "
                    "IMPORTANT: Execute tools ONE AT A TIME. Do not attempt to call multiple tools in a single turn. "
                    "Wait for the result of one tool before calling the next."
                ),
            },
            {"role": "user", "content": prompt},
        ]

        # Allow up to 5 steps of 'thinking' and 'acting'
        for _ in range(5):
            response = await self.groq.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                tools=tools if tools else None,
                tool_choice="auto",
            )

            response_message = response.choices[0].message
            messages.append(response_message)

            # If no more tools are called, we are finished!
            if not response_message.tool_calls:
                return response_message.content

            # Handle multiple tool calls in one turn
            for tool_call in response_message.tool_calls:
                name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)

                print(f"🛠️  Agent calling tool: {name}")

                # Look up which server owns this tool
                session = self.tool_map.get(name)
                if not session:
                    tool_result = f"Error: Tool {name} not found."
                else:
                    result = await session.call_tool(name, args)
                    tool_result = result.content[0].text

                # Feed the tool result back to the LLM
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": tool_result,
                    }
                )

        last_msg = messages[-1]

        # If the last message is an object (from the Groq SDK)
        if hasattr(last_msg, "content"):
            return last_msg.content or "Task completed via tools."

        # If the last message is a dictionary (from our tool result append)
        if isinstance(last_msg, dict):
            return f"Task complete. Last result: {last_msg.get('content')}"

        return "Task completed."

    async def cleanup(self):
        """Shuts down all server connections cleanly."""
        print("\n🛑 Shutting down servers...")
        await self.exit_stack.aclose()
