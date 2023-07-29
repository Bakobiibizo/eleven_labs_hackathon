#api end points for /image /text /voice
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIWebSocketRoute, Mount

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
)

@app.websocket("/text")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        # Handle the received text data here

@app.websocket("/updates")
async def websocket_update_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        # Send updates to the UI here
        # You will need to implement the logic for sending MP3 and JPG files
