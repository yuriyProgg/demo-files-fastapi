from fastapi import FastAPI
from posts import post_router
from media import media_router


app = FastAPI(
    title="Demo FastAPI",
    description="Demo FastAPI for posts with images",
    version="0.1.0",
    root_path="/api",
)

app.include_router(media_router)
app.include_router(post_router)
