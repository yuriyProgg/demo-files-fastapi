import json

from posts.schemas import PostCreateSchema, PostResponseSchema
from utils.annotations import PostDep

from fastapi import APIRouter, HTTPException, UploadFile, Form, status

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post(
    "", response_model=PostResponseSchema
)  # Укажите вашу Pydantic-модель для ответа
async def create_post(image: UploadFile, post: PostDep, data: str = Form(...)):
    try:
        json_data = json.loads(data)
        new_post = PostCreateSchema(**json_data)
        result = await post.create(image, new_post)
        return result  # FastAPI сериализует result в JSON
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Некорректный JSON",
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )


@router.get("")
async def get_all_posts(post: PostDep):
    return await post.find_all()


@router.get("/{post_id}")
async def get_post(post_id: int, post: PostDep):
    return await post.find_by_id(post_id)


@router.delete("/{post_id}")
async def delete_post(post_id: int, post: PostDep):
    return await post.delete(post_id)
