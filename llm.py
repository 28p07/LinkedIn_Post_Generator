from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
import os

llm = ChatGroq(model_name = "llama3-70b-8192",groq_api_key = os.getenv("GROQ_API_KEY"))