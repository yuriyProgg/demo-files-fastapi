from pydantic import BaseModel


class PostCreateSchema(BaseModel):
    content: str


class PostResponseSchema(BaseModel):
    post_id: int
