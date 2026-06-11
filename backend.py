from llama_index.core import SimpleDirectoryReader 
from llama_index.llms.groq import Groq
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import os
from dotenv import load_dotenv
from llama_index.core import Settings, VectorStoreIndex 

load_dotenv()

Settings.embed_model=HuggingFaceEmbedding(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

Settings.llm=Groq(
        model=os.getenv("GROQ_MODEL"),
        api_key=os.getenv("GROQ_KEY")
)

def create_index(pdf_path):


    documents=SimpleDirectoryReader(
        input_files=[pdf_path]
    ).load_data()

    index=VectorStoreIndex.from_documents(documents)

    return index

def ask_question(index,question):
    query_engine=index.as_query_engine()

    response=query_engine.query(question)

    return str(response)