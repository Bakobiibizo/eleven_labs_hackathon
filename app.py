#api end points for /image /text /voice
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIWebSocketRoute, Mount

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
)
