from pydantic import BaseModel

class BlogPostBase(BaseModel):
    title: str
    author: str
    content: str

class BlogPostCreate(BlogPostBase):
    pass

class BlogPostResponse(BlogPostBase):
    id: int

    class Config:
        orm_mode = True
