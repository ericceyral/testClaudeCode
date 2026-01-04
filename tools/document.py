import os
from markitdown import MarkItDown, StreamInfo
from io import BytesIO
from pydantic import Field


def binary_document_to_markdown(binary_data: bytes, file_type: str) -> str:
    """Converts binary document data to markdown-formatted text."""
    md = MarkItDown()
    file_obj = BytesIO(binary_data)
    stream_info = StreamInfo(extension=file_type)
    result = md.convert(file_obj, stream_info=stream_info)
    return result.text_content


def document_path_to_markdown(
    file_path: str = Field(description="Absolute path to a PDF or DOCX file to convert"),
) -> str:
    """Convert a PDF or DOCX file to markdown.

    Reads a document file from the given path and converts its content to
    markdown-formatted text using the MarkItDown library.

    When to use:
    - When you need to extract text content from PDF or DOCX files
    - When you want document content in a readable markdown format

    When not to use:
    - For unsupported file types (only .pdf and .docx are supported)
    - For very large files that may cause memory issues

    Examples:
    >>> document_path_to_markdown("/path/to/document.docx")
    "# Document Title\\n\\nDocument content here..."
    >>> document_path_to_markdown("/path/to/report.pdf")
    "# Report\\n\\nReport content..."
    """
    supported_extensions = {".pdf", ".docx"}

    _, ext = os.path.splitext(file_path)
    ext = ext.lower()

    if ext not in supported_extensions:
        raise ValueError(f"Unsupported file type: {ext}. Supported types: {supported_extensions}")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "rb") as f:
        binary_data = f.read()

    file_type = ext.lstrip(".")
    return binary_document_to_markdown(binary_data, file_type)
