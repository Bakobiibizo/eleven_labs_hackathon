import uvicorn
from fastapi import FastAPI, requests
from fastapi.middleware.cors import CORSMiddleware
from data_handler import DataHandler
from typing import Optional


handler = DataHandler()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
)

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

@app.get("/update")
def update(mode, item)-> str:
    response = requests.get(f"http://127.0.0.1:8000/{mode}", json={"mode": mode, "item": item})
    return response.json()  

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080, log_level="info")