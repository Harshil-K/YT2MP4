# pylint: skip-file

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from downloadAPI import downloadVideo
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


import uuid

app = FastAPI()

class URLRequest(BaseModel):
    url: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",        # React dev server
        "http://127.0.0.1:3000",        # Alternate local access
        "http://localhost:8000",        # Optional for testing
        "http://127.0.0.1:8000",        # Optional for testing
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/download")
async def download(data: URLRequest):
    filename = downloadVideo(data.url)
    return FileResponse(filename, media_type="video/mp4", filename="video.mp4")

app.mount("/", StaticFiles(directory="../Frontend/my-youtube-app", html=True), name="Frontend")