<div align="center">

# 🤖 Clarus (ExaBytes RAG Demo Application)

![Python](https://img.shields.io/badge/python-v3.11+-blue.svg)
![Flask](https://img.shields.io/badge/flask-v3.0.0-lightgrey.svg)
![LangChain](https://img.shields.io/badge/langchain-v0.1.0-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

A modern web application implementing Retrieval Augmented Generation (RAG) using Flask and Tailwind CSS. Upload documents and get AI-powered answers based on their content.

[Features](#features) •
[Quick Start](#quick-start) •
[Installation](#installation) •
[Usage](#usage) •
[Architecture](#architecture) •
[Development](#development)

</div>

## ✨ Features

- 📄 **Document Processing**
  - Support for PDF and TXT files
  - Automatic text chunking and embedding
  - Efficient vector storage with ChromaDB

- 🔍 **Advanced RAG Implementation**
  - Powered by Groq's Mixtral-8x7b model
  - Sentence transformers for embeddings
  - Context-aware question answering

- 🎨 **Modern UI/UX**
  - Clean, responsive design with Tailwind CSS
  - Real-time loading states
  - Toast notifications for feedback
  - Drag-and-drop file upload

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/clarus.git
cd clarus

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
uv pip install -e .

# Set up environment variables
cp app/.env.example app/.env
# Edit app/.env with your API keys

# Run the application
python main.py
```

Visit `http://localhost:5000` in your browser to start using the application.

## 🛠️ Installation

### Prerequisites

- Python 3.11+
- uv package manager (recommended) or pip
- Groq API key for LLM access

### Detailed Setup

1. **Environment Setup**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install Dependencies**
   
   Using uv (recommended):
   ```bash
   uv pip install -e .
   ```
   
   Using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**
   ```bash
   cp app/.env.example app/.env
   ```
   Edit `app/.env` and add:
   ```
   SECRET_KEY=your-secret-key
   GROQ_API_KEY=your-groq-api-key
   ```

## 🎯 Usage

1. **Upload Documents**
   - Click the upload area or drag and drop files
   - Supported formats: PDF, TXT
   - Wait for the success notification

2. **Ask Questions**
   - Enter your question in the text area
   - Click "Get Answer"
   - View AI-generated response based on your documents

## 🏗️ Architecture

```
.
├── app/                  # Application package
│   ├── templates/       # HTML templates
│   ├── static/         # Static files
│   ├── utils/          # Utility modules
│   │   └── rag.py     # RAG implementation
│   └── routes.py       # Flask routes
├── main.py             # Application entry point
├── pyproject.toml      # Project metadata and dependencies
└── requirements.txt    # Direct dependencies
```

## 🧪 Development

### Tech Stack

- **Backend**
  - Flask: Web framework
  - LangChain: RAG implementation
  - ChromaDB: Vector storage
  - Sentence Transformers: Text embeddings
  - Groq: LLM provider

- **Frontend**
  - Tailwind CSS: Styling
  - Vanilla JavaScript: Interactivity

### Development Tools

```bash
# Install development dependencies
uv pip install -e ".[dev]"

# Format code
black app/
isort app/

# Lint code
flake8 app/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
Made with ❤️ using Flask, LangChain, and Groq
</div>