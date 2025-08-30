from core.database import Model

from sqlalchemy.orm import Mapped


class Post(Model):
    __tablename__ = "posts"

    content: Mapped[str]
    image_url: Mapped[str]
