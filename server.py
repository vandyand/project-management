# server.py

from fastapi import FastAPI
from interpreter import interpreter
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
    
interpreter.auto_run = True
interpreter.llm.model = "gpt-4o-mini"
interpreter.llm.api_key = os.getenv("OPENAI_API_KEY")
interpreter.loop = True

@app.get("/chat")
def chat_endpoint(message: str):
    return interpreter.chat(message)

@app.get("/history")
def history_endpoint():
    return interpreter.messages
