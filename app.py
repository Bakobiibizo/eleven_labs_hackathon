from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIWebSocketRoute, Mount

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
)

from voice.eleven_labs import TextToSpeach
from text.create_messages import Messages
from text.openai_text import OpenAITextGeneration
from text.message_defs import RoleOptions
import base64

tts = TextToSpeach()
messages = Messages()
openai_text = OpenAITextGeneration()

@app.websocket("/text")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()


@app.websocket("/updates")
async def websocket_update_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        # Send updates to the UI here
        # You will need to implement the logic for sending MP3 and JPG files
        # For now, we will just send the base64 audio
        await websocket.send_text(audio_base64)
