from utils.repositories import SQLAlchemyRepository
from .models import Post


class PostRepository(SQLAlchemyRepository):
    model = Post
