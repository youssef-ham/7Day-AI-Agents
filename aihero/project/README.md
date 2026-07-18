# 🦜 LangChain Docs Assistant

An AI-powered documentation assistant that answers questions about **LangChain**, **LangGraph**, and **LangSmith** using Retrieval-Augmented Generation (RAG).

The application indexes the official LangChain documentation repository, retrieves the most relevant sections using full-text search, and generates answers with Groq's `openai/gpt-oss-120b` model.

---

## 🚀 Demo

**Live App:** https://YOUR-STREAMLIT-APP.streamlit.app

**GitHub Repository:** https://github.com/YOUR_USERNAME/YOUR_REPOSITORY

---

## ✨ Features

- 📚 Search across LangChain documentation
- 🔎 Retrieval-Augmented Generation (RAG)
- 🤖 AI-powered answers using Groq
- ⚡ Fast full-text search with MinSearch
- 💬 Simple Streamlit chat interface
- 📄 References to the original documentation

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Groq API
- MinSearch
- Python Frontmatter
- Requests

---

## 📂 Project Structure

```
.
├── app.py
├── ingest.py
├── search_agent.py
├── search_tools.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git

cd YOUR_REPOSITORY
```

Create a virtual environment:

```bash
uv venv
```

Activate it:

Linux / macOS

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
uv pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run

```bash
streamlit run app.py
```

or

```bash
uv run streamlit run app.py
```

---

## 📸 Screenshot

_Add a screenshot of the application here._

---

## 📖 Example Questions

- How do I create an AI agent in LangChain?
- What is LangGraph?
- How do I use LangSmith?
- How do I create tools in LangChain?
- What is LCEL?

---

## 📄 License

This project is for educational purposes.