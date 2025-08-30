from typing import Annotated
from fastapi import Depends
from posts.service import PostService
from utils.dependencies import post_service

PostDep = Annotated[PostService, Depends(post_service)]
