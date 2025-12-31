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

3. Usage
   Run the client and point it toward an MCP server (e.g., GitHub or Brave):

   Python

   `python client.py`
