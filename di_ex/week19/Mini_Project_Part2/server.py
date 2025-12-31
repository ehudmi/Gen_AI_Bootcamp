import os
from fastmcp import FastMCP

# 1. Initialize FastMCP
mcp = FastMCP("NotesManager")

# 2. Setup Absolute Path for the notes folder
# This ensures that even if you run main.py from a different folder,
# the notes always go to the right place.
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
NOTES_DIR = os.path.join(CURRENT_DIR, "notes")

# Ensure the directory exists
os.makedirs(NOTES_DIR, exist_ok=True)


@mcp.tool()
def save_note(name: str, content: str) -> str:
    """
    Saves a new note to the local 'notes' directory.
    Args:
        name: The filename (without .txt extension).
        content: The text content to write into the note.
    """
    try:
        file_path = os.path.join(NOTES_DIR, f"{name}.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"✅ Successfully saved note to: {file_path}"
    except Exception as e:
        return f"❌ Error saving note: {str(e)}"


@mcp.tool()
def read_notes() -> str:
    """
    Lists all available notes and their content summaries from the local directory.
    """
    try:
        files = [f for f in os.listdir(NOTES_DIR) if f.endswith(".txt")]
        if not files:
            return "No notes found in the directory."

        return "Available Notes: " + ", ".join(files)
    except Exception as e:
        return f"❌ Error reading directory: {str(e)}"


if __name__ == "__main__":
    mcp.run()
