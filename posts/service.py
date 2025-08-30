import os
from datetime import datetime

from utils.repositories import AbstractRepository
from core.settings import MEDIA_ROOT, MEDIA_URL
from posts.schemas import PostCreateSchema
from posts.models import Post

from fastapi import HTTPException, UploadFile, status


class PostService:
    def __init__(self, repository: AbstractRepository):
        self.__repo = repository

        if not os.path.exists(MEDIA_ROOT):
            os.makedirs(MEDIA_ROOT)

    async def create(self, image: UploadFile, data: PostCreateSchema):
        file = image.file
        *filename, file_extension = str(image.filename).split(".")
        new_filename = (
            "".join(filename)
            + datetime.now().strftime("%Y%m%d%H%M%S")
            + "."
            + file_extension
        )
        with open(MEDIA_ROOT / new_filename, "wb") as f:
            f.write(file.read())
        post_id = await self.__repo.create(
            content=data.content,
            image_url=f"{MEDIA_URL}{new_filename}",
        )
        return {"post_id": post_id}

    async def find_all(self):
        return await self.__repo.find_all()

    async def find_by_id(self, id: int) -> Post:
        post = await self.__repo.find_one(Post.id == id)
        if not post:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Пост не найден",
            )
        return post

    async def delete(self, id: int):
        post = await self.find_by_id(id)
        await self.__repo.delete(Post.id == post.id)
