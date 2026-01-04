# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Setup (requires Python 3.12 or 3.13 - Python 3.14+ not supported due to onnxruntime)
uv venv --python 3.12
uv pip install -e .

# Run the MCP server
uv run main.py

# Run all tests
uv run pytest

# Run a single test file
uv run pytest tests/test_document.py

# Run a specific test
uv run pytest tests/test_document.py::TestBinaryDocumentToMarkdown::test_binary_document_to_markdown_with_docx
```

## Architecture

This is an MCP (Model Context Protocol) server that exposes document processing tools to AI assistants.

**Entry point:** `main.py` - Creates a FastMCP server instance and registers tools via `mcp.tool()(function_name)`.

**Tools directory:** `tools/` - Contains tool implementations as standalone Python functions. Each tool function is imported into `main.py` and registered with the MCP server.

## Defining MCP Tools

Tools are Python functions registered with the MCP server using:

```python
mcp.tool()(my_function)
```

### Tool Docstrings

Tool descriptions should include:
- One-line summary
- Detailed explanation of functionality
- When to use (and not use) the tool
- Usage examples with expected input/output

### Parameter Descriptions

Use `Field` from pydantic for parameter descriptions:

```python
from pydantic import Field

def my_tool(
    param1: str = Field(description="Detailed description of this parameter"),
    param2: int = Field(description="Explain what this parameter does")
) -> ReturnType:
    """Comprehensive docstring here"""
    # Implementation
```

See `tools/math.py` for a complete example of a well-documented tool.
