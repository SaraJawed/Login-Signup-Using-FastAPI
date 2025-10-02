from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    full_name: str | None = None

class UserCreate(UserBase):
    password: str
    is_admin: bool = False   # ✅ Add here

class UserOut(UserBase):
    id: int
    is_admin: bool           # ✅ Add here

class Config:
    from_attributes = True

