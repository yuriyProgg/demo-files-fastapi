from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from posts import post_router
from media import media_router


app = FastAPI(
    title="Demo FastAPI",
    description="Demo FastAPI for posts with images",
    version="0.1.0",
    root_path="/api",
)

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Разрешаем только ваш frontend
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем все методы (GET, POST, и т.д.)
    allow_headers=["*"],  # Разрешаем все заголовки
)


# Роутеры
app.include_router(media_router)
app.include_router(post_router)
