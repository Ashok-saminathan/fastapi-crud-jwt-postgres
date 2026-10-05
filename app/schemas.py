from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr

# ---------- User ----------
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)

# ---------- Token ----------
class Token(BaseModel):
    access_token: str
    token_type: str
    username: str

# ---------- Item ----------
class ItemCreate(BaseModel):
    title: str
    description: Optional[str] = None

class ItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class ItemOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    owner_id: int

    model_config = ConfigDict(from_attributes=True)