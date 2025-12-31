# MCP Part 1: Agnostic Client Implementation

## Overview

This project implements a robust, asynchronous MCP Client designed to connect to any standard MCP server. The primary focus of this phase was handling the lifecycle of MCP sessions and managing asynchronous communication on Windows.

## Features

- **Generic Connection:** Supports any server following the Stdio transport protocol.
- **Dynamic Tool Discovery:** Automatically lists and formats tools for LLM integration.
- **Async Robustness:** Implements `AsyncExitStack` for clean resource management and process termination.
- **Provider Support:** Configured to use GroqCloud (Llama 3) as the reasoning engine.

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your API Key:
   'DOS'
   `set GROQ_API_KEY=your_key_here`

### 3. README.md for Part 2: Custom Server & Orchestration

> **Focus:** Proving you can build your own tools and coordinate multiple servers.

````markdown
# MCP Part 2: Custom Server & Multi-Server Orchestration

## Overview

This project expands on the MCP framework by introducing a custom-built Python server and a multi-server orchestrator. The agent can now "think" across multiple domains—searching the web via Brave, checking code on GitHub, and managing local files via a custom Notes server.

## Components

1. **Custom Notes Server:** Built with `FastMCP`, providing tools to `save_note` and `read_notes` to the local filesystem.
2. **Multi-Server Orchestrator:** A central agent that maintains active sessions with three concurrent servers.
3. **Sequential Planning:** Uses a specialized system prompt to ensure the LLM executes complex tool chains (Search -> Read -> Write) reliably.

## Custom Tools

- `save_note(name, content)`: Persists research data to the `/notes` directory.
- `read_notes()`: Allows the LLM to audit existing local data before taking action.

## Setup & Execution

1. **Install Servers:**
   Ensure Node.js servers for GitHub and Brave are installed globally:
   ```bash
   npm install -g @modelcontextprotocol/server-github @modelcontextprotocol/server-brave-search
   ```
2. Environment Variables: Ensure GROQ_API_KEY, GITHUB_TOKEN, and BRAVE_API_KEY are set.

3. Run the Orchestrator:

   `python main.py`
````

# Requirements

1. fastmcp: For the server implementation.

2. mcp: For the client-server protocol.

3. groq: For the Llama 3.3-70b reasoning.
