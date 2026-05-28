# 🦜 LangChain URL & YouTube Summarizer

An AI-powered summarization application built using **LangChain**, **Groq**, and **Streamlit**.

This app can summarize:

* 🎥 YouTube Videos
* 🌐 Website URLs
* 📰 Blog Articles
* 📚 Documentation Pages
* 🗞️ News Websites

using **LLM-powered summarization pipelines** with LangChain LCEL.

---

# 🚀 Features

* Summarize YouTube video transcripts
* Summarize website content
* Fast inference using Groq LLMs
* Streamlit-based modern UI
* LCEL (LangChain Expression Language) pipeline
* URL validation support
* Supports long-form content summarization

---

# 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* LangChain LCEL
* Groq API
* YouTube Transcript API
* Unstructured URL Loader

---

# 📂 Project Structure

```bash
LangChain-URL-YT-Summarizer/
│
├── ui.py
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/LangChain-URL-YT-Summarizer.git

cd LangChain-URL-YT-Summarizer
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

Get your API key from:

https://console.groq.com/

---

# ▶️ Run Application

```bash
streamlit run ui.py
```

OR

```bash
python -m streamlit run ui.py
```

---

# 📸 Application Preview

## Home Screen

* Enter Groq API Key
* Paste YouTube or Website URL
* Click "Summarize Content"

## Output

* AI-generated concise summary
* Key insights
* Main conclusions

---

# 🧠 Supported Models

Example:

```python
model="llama-3.1-8b-instant"
```

You can also use:

* llama3-70b
* mixtral
* gemma
* deepseek models (if supported)

---

# 📦 Requirements

Example dependencies:

```txt
streamlit
langchain
langchain-core
langchain-community
langchain-groq
youtube-transcript-api
unstructured
validators
python-dotenv
```

---

# 🔥 How It Works

## YouTube Flow

1. Extract Video ID
2. Fetch transcript
3. Convert transcript to text
4. Send content to LLM
5. Generate summary

---

## Website Flow

1. Load webpage using UnstructuredURLLoader
2. Extract textual content
3. Pass content to LCEL chain
4. Generate AI summary

---

# 🧩 LCEL Chain

```python
chain = prompt | llm | output_parser
```

This pipeline:

* formats the prompt
* sends request to LLM
* parses output

---

# 📚 Learning Concepts Used

* LangChain LCEL
* Prompt Engineering
* Output Parsers
* LLM Integration
* Document Processing
* AI Summarization
* Streamlit UI

---

# ⚠️ Common Errors

## ModuleNotFoundError

Install missing packages:

```bash
pip install -r requirements.txt
```

---

## Streamlit Using Wrong Python

Run:

```bash
python -m streamlit run ui.py
```

instead of:

```bash
streamlit run ui.py
```

---

# 🤝 Contributing

Pull requests are welcome.

For major changes, open an issue first to discuss what you would like to change.

---

# 📄 License

MIT License

---

# 👨‍💻 Author

Prajwal Tripathi

Built with ❤️ using LangChain + Groq + Streamlit
