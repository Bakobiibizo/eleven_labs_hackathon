from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data_handler import DataHandler, RoleOptions
from typing import Coroutine, Any, List

handler = DataHandler()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
)

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/text")
def text(content: str, role: RoleOptions=None) -> str:
    return handler.generate_text(role=role, content=content)

@app.get("/voice")
def voice(message: str, voice_id: str) -> str:
    return handler.generate_voice(message=message, voice_id=voice_id)

@app.get("/image")
async def image(prompt: str=None) -> str:
    return await handler.generate_image(prompt=prompt)
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)