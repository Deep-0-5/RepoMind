# RepoMind

<p align="center">
  <strong>AI-Powered Repository Understanding Assistant</strong><br>
  Understand any codebase using <strong>Retrieval-Augmented Generation (RAG)</strong>,
  <strong>Google Gemini</strong>, <strong>Sentence Transformers</strong>, and <strong>ChromaDB</strong>.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?logo=streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-4285F4?logo=google&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Database-16A085)
![RAG](https://img.shields.io/badge/RAG-Retrieval--Augmented--Generation-6C5CE7)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

---

## Overview

RepoMind is an AI-powered repository understanding assistant that enables developers to explore, understand, and interact with software codebases using natural language.

Instead of manually navigating hundreds of source files, developers can simply ask questions such as:

- How is authentication implemented?
- Explain the project architecture.
- Where is the login API?
- Summarize this repository.
- Which files implement database models?

RepoMind combines **Retrieval-Augmented Generation (RAG)**, **Google Gemini Large Language Models (LLMs)**, **semantic vector search**, and embedding models to generate context-aware answers about software repositories with references to relevant source files.

---

# Why RepoMind?

Understanding a new codebase is one of the biggest challenges for developers.

RepoMind simplifies repository exploration by converting source code into semantic embeddings, storing them in a vector database, and allowing developers to query the repository using natural language.

It acts as an intelligent AI assistant capable of understanding project structure, explaining code, and helping developers navigate unfamiliar repositories more efficiently.

---

# Features

| Feature | Status |
|----------|:------:|
| Repository Parsing | ✅ |
| Local Repository Support | ✅ |
| GitHub Repository Support | ✅ |
| Python AST-based Chunking | ✅ |
| Generic Code Chunking | ✅ |
| Incremental Repository Indexing | ✅ |
| SHA-256 Change Detection | ✅ |
| Google Gemini Integration | ✅ |
| Sentence Transformer Embeddings | ✅ |
| ChromaDB Vector Database | ✅ |
| Semantic Vector Search | ✅ |
| Retrieval-Augmented Generation (RAG) | ✅ |
| AI-powered Repository Chat | ✅ |
| Source File References | ✅ |
| Repository Statistics | ✅ |
| Persistent Chat Sessions | ✅ |
| Interactive Streamlit Dashboard | ✅ |

---

# Architecture

```text
                    Repository
                         │
                         ▼
                 Repository Parser
                         │
                         ▼
                  File Reader
                         │
                         ▼
                  Chunk Manager
              ┌──────────┴──────────┐
              ▼                     ▼
      Python AST Chunker     Generic Chunker
              │
              ▼
            Embeddings
      ┌──────────┴──────────┐
      ▼                     ▼
 Google Gemini      Sentence Transformers
              │
              ▼
             ChromaDB
              │
              ▼
            Retriever
              │
              ▼
        Context Builder
              │
              ▼
       Gemini Generator
              │
              ▼
        Streamlit Interface
```

---

# Project Structure

```text
repo-ai-assistant/

├── assets/                 # Custom styles and UI assets
├── data/                   # Runtime generated data
├── embeddings/             # Embedding providers
├── indexing/               # Repository indexing pipeline
├── models/                 # Data models
├── processing/             # Chunking pipeline
├── rag/                    # Retrieval-Augmented Generation
├── repository/             # Repository parser & GitHub cloning
├── scripts/                # Manual verification scripts
├── tests/                  # Unit tests
├── ui/                     # Streamlit UI
├── utils/                  # Utilities and shared resources
├── vector_db/              # ChromaDB implementation

├── app.py                  # Streamlit entry point
├── main.py                 # Main application
├── requirements.txt
├── README.md
└── TODO.md
```

---

# Tech Stack

| Category | Technologies |
|-----------|--------------|
| **Programming Language** | Python |
| **Frontend** | Streamlit |
| **Large Language Model (LLM)** | Google Gemini 2.5 Flash |
| **Embeddings** | Google Gemini Embeddings, Sentence Transformers (BAAI/bge-small-en-v1.5) |
| **Vector Database** | ChromaDB |
| **Retrieval Framework** | Retrieval-Augmented Generation (RAG) |
| **Code Parsing** | Python AST, Generic File Parser |
| **Repository Processing** | Local Repository, GitHub Repository |
| **Version Control** | Git, GitHub |
| **Testing** | Pytest |
| **Configuration** | Python Dotenv |
| **Logging** | Custom Logging Module |

---

# Installation

## Clone the repository

```bash
git clone https://github.com/Deep-0-5/RepoMind.git
cd RepoMind
```

## Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Copy the example environment file:

```bash
cp .env.example .env
```

Then edit `.env` and add your Gemini API key.

## Run the application

```bash
streamlit run app.py
```

---

# Usage

1. Launch the Streamlit application.
2. Select a local repository or provide a GitHub repository URL.
3. Index the repository.
4. Wait for indexing to complete.
5. Ask questions about the repository using natural language.
6. Receive AI-generated responses with relevant source file references.

---

# Example Questions

- Explain this project.
- Summarize the repository architecture.
- How many Python files are in this project?
- Where is authentication implemented?
- Explain the indexing pipeline.
- Which files define API endpoints?
- Show repository statistics.
- Explain the embedding workflow.

---

# Roadmap

## Repository Understanding

- Repository summarization
- Architecture explanation
- Dependency analysis
- File relationship graph

## Retrieval Improvements

- Hybrid Search
- Similarity Threshold
- Multi-query Retrieval
- Re-ranking

## AI Features

- Bug Detection
- Documentation Generation
- UML Diagram Generation
- API Documentation Generator
- Refactoring Suggestions

## GitHub Integration

- Private Repository Support
- Branch Selection
- Repository Synchronization

## Future Enhancements

- Multi-language Support
- VS Code Extension
- REST API
- MCP Server
- Voice Assistant
- Multi-Repository Chat

---

# Testing

RepoMind includes comprehensive unit tests covering:

- Repository Parsing
- Chunking
- Embeddings
- ChromaDB
- Repository Indexing
- Retrieval
- Context Building
- Generator
- Chat Engine

Run all tests:

```bash
pytest
```

---

# Contributing

Contributions, feature requests, and suggestions are welcome.

If you find a bug or have an idea for improvement, feel free to open an issue or submit a pull request.

---

# License

This project is licensed under the MIT License.

---

# Acknowledgements

- Google Gemini
- ChromaDB
- Sentence Transformers
- Streamlit
- Python Community

---

<p align="center">
Made with ❤️ using Python, RAG, Google Gemini, and Streamlit.
</p>