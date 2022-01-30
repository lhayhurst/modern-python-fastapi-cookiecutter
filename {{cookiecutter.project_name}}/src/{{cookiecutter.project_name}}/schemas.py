from typing import List

from pydantic import BaseModel


class MicroBlogPostBase(BaseModel):
    title: str
    content: str


class MicroBlogPostCreate(MicroBlogPostBase):
    pass


class MicroBlogPost(MicroBlogPostBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    micro_blog_posts: List[MicroBlogPost] = []

    class Config:
        orm_mode = True
