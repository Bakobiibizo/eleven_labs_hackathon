#api end points for /image /text /voice
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIWebSocketRoute, Mount

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
)

from voice.eleven_labs import TextToSpeach
import base64

tts = TextToSpeach()

@app.websocket("/text")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        # Generate audio from the received text
        audio_file = tts.tts(data, voice_id=None)
        # Convert the audio file to base64
        with open(audio_file, "rb") as f:
            audio_base64 = base64.b64encode(f.read())
        # Send the base64 audio to the UI
        await websocket.send_text(audio_base64)

@app.websocket("/updates")
async def websocket_update_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        # Send updates to the UI here
        # You will need to implement the logic for sending MP3 and JPG files
        # For now, we will just send the base64 audio
        await websocket.send_text(audio_base64)
