from pydantic import BaseModel, EmailStr
class UserBase(BaseModel):
    email: EmailStr
    username: str
class UserCreate(UserBase):
    password: str
class User(UserBase):
    id: int