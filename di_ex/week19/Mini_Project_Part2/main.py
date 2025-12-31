import asyncio
import os
from client import (
    LeanMCPAgent,
)  # We will slightly update this to handle multiple connects

node_modules_path = r"C:\nvm4w\nodejs\node_modules"

print(f"DEBUG: Brave Key Found? {'Yes' if 'BRAVE_API_KEY' in os.environ else 'No'}")


async def main():
    agent = LeanMCPAgent()

    try:
        print("🚀 Booting MCP Orchestrator...")

        # 1. Connect to ALL 3 Servers
        # Note: We'll update LeanMCPAgent.connect to be callable multiple times
        # 1. Connect to GitHub (Directly using Node)
        github_path = os.path.join(
            node_modules_path,
            "@modelcontextprotocol",
            "server-github",
            "dist",
            "index.js",
        )
        await agent.connect_server("github", "node", [github_path])

        # 2. Connect to Brave (Directly using Node)
        brave_path = os.path.join(
            node_modules_path,
            "@modelcontextprotocol",
            "server-brave-search",
            "dist",
            "index.js",
        )
        await agent.connect_server("brave", "node", [brave_path])

        # 3. Connect to your local Notes server
        await agent.connect_server("notes", "python", ["server.py"])

        print("✅ GitHub, Brave, and Notes servers online.")

        # 2. The Multi-Step Challenge
        # This requires the LLM to: Search (Brave/GitHub) -> Read (Notes) -> Save (Notes)
        prompt = (
            "Check my local notes to see if I have a project plan. "
            "Then, search GitHub for the 'modelcontextprotocol/python-sdk' repo description. "
            "Finally, create a new note called 'Research_Results' that combines my plan with the repo info."
        )

        print(f"\n💬 User: {prompt}\n")
        response = await agent.chat(prompt)
        print(f"🤖 Assistant: {response}")

    finally:
        await agent.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
