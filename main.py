import uvicorn

from data_handler import DataHandler
from typing import Optional
from flask import Flask, Request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

handler = DataHandler()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/chat")
def chat(content: str, role: Optional[str]) -> str:
    return handler.handle_chat(content=content, role=role)

@app.get("/text")
def text(content: str, role: Optional[str]) -> str:
    return handler.handle_chat(role=role, content=content)

@app.get("/voice")
def voice(message: str, voice_id: str) -> str:
    return handler.handle_voice(message=message, voice_id=voice_id)

@app.get("/image")
def image(prompt: str) -> str:
    return handler.handle_image(prompt=prompt)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080, log_level="info")