# 🤖 AI FAQ Assistant

An AI-powered documentation assistant built with **Streamlit** and **Groq LLMs**. The application indexes the DataTalksClub FAQ repository and allows users to ask questions in natural language and receive contextual answers with references to the original documentation.

## 🚀 Live Demo

🔗 https://7day-ai-agents-gd6jzxgze7juantnkl8bvj.streamlit.app/

## 📂 GitHub Repository

🔗 https://github.com/youssef-ham/7Day-AI-Agents/blob/main/aihero/course

---

## ✨ Features

- Ask questions about the DataTalksClub FAQ repository.
- Semantic search over documentation.
- AI-generated answers using Groq LLMs.
- References and links to the original source files.
- Simple and interactive Streamlit interface.

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Groq API
- Vector Search / Text Search
- Git & GitHub
- UV Package Manager

---

## 📁 Project Structure

```text
.
├── app.py
├── ingest.py
├── ingest_chunk.py
├── search_agent.py
├── search_tools.py
├── logs.py
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/youssef-ham/7Day-AI-Agents.git
cd 7Day-AI-Agents/aihero/course
```

### 2. Create a virtual environment

```bash
uv venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
uv sync
```

or

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

or

```bash
uv run streamlit run app.py
```

---

## ☁️ Deploy on Streamlit Cloud

1. Push the project to GitHub.
2. Create a new app on Streamlit Cloud.
3. Set the main file path:

```text
aihero/course/app.py
```

4. Add the following secret:

```toml
GROQ_API_KEY="your_groq_api_key"
```

---

## 📸 Demo

Add screenshots of your application here.

### Home Page

![App Screenshot](images/app.png)

---

## 📈 Future Improvements

- Add vector embeddings.
- Support multiple repositories.
- Conversation memory.
- Source highlighting and citations.
- User authentication.

---

## 👨‍💻 Author

**Youssef Fawzy**

- LinkedIn: https://www.linkedin.com/posts/youssef-fawzy-ai
- GitHub: https://github.com/youssef-ham

---

⭐ If you found this project useful, consider giving it a star.