import streamlit as st
import asyncio
import nest_asyncio
from client import StandaloneMCPAgent

# 1. Patch asyncio to allow nesting (Required for Streamlit)
nest_asyncio.apply()

st.set_page_config(page_title="MCP Researcher", page_icon="🕵️")
st.title("🕵️ MCP Research Agent")

import logging

logging.basicConfig(level=logging.DEBUG)


# 2. Persist the agent across reruns
@st.cache_resource
def initialize_global_agent():
    return StandaloneMCPAgent()


agent = initialize_global_agent()

# Initialize session state
if "connected" not in st.session_state:
    st.session_state.connected = False
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- CONNECTION HEADER ---
if not st.session_state.connected:
    with st.status("🚀 Starting MCP Servers...", expanded=True) as status:
        # We get the current loop and use it to run our async tasks
        loop = asyncio.get_event_loop()

        st.write("Connecting to GitHub (Windows Fix)...")
        # WINDOWS FIX: Use cmd /c to ensure npx is found and executed correctly
        loop.run_until_complete(
            agent.connect_server(
                "github",
                "cmd",
                ["/c", "npx", "-y", "@modelcontextprotocol/server-github"],
            )
        )

        st.write("Connecting to Brave (Windows Fix)...")
        loop.run_until_complete(
            agent.connect_server(
                "brave",
                "cmd",
                ["/c", "npx", "-y", "@modelcontextprotocol/server-brave-search"],
            )
        )

        status.update(label="✅ Servers Online!", state="complete", expanded=False)
        st.session_state.connected = True

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- CHAT INTERACTION ---
if prompt := st.chat_input("Ask about a GitHub repo or search the web..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.status("Agent is researching...", expanded=True) as status:
            st.write("Reasoning with Llama 3.3...")

            # Execute the agent chat using the existing loop
            loop = asyncio.get_event_loop()
            response = loop.run_until_complete(agent.chat(prompt))

            status.update(label="✨ Research Complete", state="complete")

        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
