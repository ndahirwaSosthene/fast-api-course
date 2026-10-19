from typing import Annotated, Optional

from pydantic import BaseModel, EmailStr, Field, conint
from datetime import datetime


class PostBase(BaseModel):
    title:  str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    # This can be helpful when we are getting an error getting a response model
    # class Config:
    #     orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None


class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(strict=True, le=1)] # this is used instead of conint which is going to be deprecated
    

