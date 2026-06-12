# AI Document Generator

Generate enterprise-grade documents instantly using LLM-powered AI with real-time streaming.

## Tech Stack

- **LangChain** — LCEL chain for prompt → LLM → output
- **Groq (LLaMA 3.3 70B)** — fast inference backend
- **Streamlit** — interactive web UI with live streaming
- **SQLite** — lightweight local history storage
- **python-docx** — DOCX export

## Features

- 5 document types: BRD, BPD, FD, TD, and Custom
- Real-time token streaming directly in the UI
- Auto-saves every generated document to local history
- Download output as `.docx` or `.txt`
- Sidebar history viewer with per-document delete

## Local Setup

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
```

Run the app:

```bash
streamlit run app.py
```
