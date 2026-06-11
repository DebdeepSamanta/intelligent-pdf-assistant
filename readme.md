# 🤖 Intelligent PDF Assistant

A simple RAG-based chatbot that lets users upload a PDF and ask questions about its contents.

Built using:

* LlamaIndex
* Groq
* Hugging Face Embeddings
* Gradio

## Features

* Upload PDF documents
* Ask questions in natural language
* Retrieve relevant information from the document
* Conversational chatbot interface
* Fast responses powered by Groq

## How to Run

1. Clone the repository
2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Add your Groq API key in a `.env` file

```env
GROQ_KEY=your_api_key
GROQ_MODEL=llama-3.1-8b-instant
```

4. Start the application

```bash
python frontendGradio.py
```

## Demo

Upload a PDF, process it, and start chatting with your document.

---

##Screenshot

<img width="1557" height="929" alt="Screenshot 2026-06-12 020647" src="https://github.com/user-attachments/assets/ad39009a-2bf5-4ed0-bc75-00bf8b609096" />


Built as a learning project to explore Retrieval-Augmented Generation (RAG) and document-based question answering.
