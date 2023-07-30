from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data_handler import DataHandler

handler = DataHandler()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
)

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/chat")
def chat(message: str, role: str) -> str:
    return handler.handle_chat(message=message, role=role)

@app.get("/text")
def text(content: str, role: str) -> str:
    return handler.handle_chat(role=role, content=content)

@app.get("/voice")
def voice(message: str, voice_id: str) -> str:
    return handler.handle_voice(message=message, voice_id=voice_id)

@app.get("/image")
def image(prompt: str) -> str:
    return handler.handle_image(prompt=prompt)
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)