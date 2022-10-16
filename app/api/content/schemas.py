from enum import Enum
from pydantic import BaseModel

class CategoryType(Enum):
    NOTICE = 'notice'
    NORMAL = 'normal'
    VOTE = 'vote'
    PRIVATE = 'private'

class Content(BaseModel):
    id: str
    title: str
    content: str
    author: list[str]
    category: CategoryType

class ContentRequest(BaseModel):
    title: str
    content: str
    author: list[str]
    category: CategoryType

class ContentResponse(BaseModel):
    id: str
    title: str
    content: str
    author: list[str]
    category: CategoryType