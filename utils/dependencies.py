from posts.service import PostService
from posts.repository import PostRepository


async def post_service():
    return PostService(PostRepository())
