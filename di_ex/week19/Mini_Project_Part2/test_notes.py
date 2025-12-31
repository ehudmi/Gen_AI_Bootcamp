import asyncio
import os
from client import LeanMCPAgent


async def main():
    # Make sure your API key is set in this terminal session!
    agent = LeanMCPAgent()

    try:
        # 1. Connect to your local server
        await agent.connect("server.py")

        # 2. Hardcoded test prompt
        print("🤖 Sending prompt to LLM...")
        prompt = "Create a note named 'success' with the content 'Streamlit was the problem!'"
        response = await agent.chat(prompt)

        print(f"📝 Agent Response: {response}")

    finally:
        await agent.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
