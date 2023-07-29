from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIWebSocketRoute, Mount
from voice.eleven_labs import TextToSpeach
from text.create_messages import Messages
from text.openai_text import OpenAITextGeneration
from text.message_defs import RoleOptions

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
)



tts = TextToSpeach()
messages = Messages()
openai_text = OpenAITextGeneration()

@app.websocket("/text")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        return "hello text"


@app.websocket("/updates")
async def websocket_update_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        return "hello updates"
