import bcrypt
from datetime import datetime
from pydantic import BaseModel, Field, EmailStr


class UserCreate(BaseModel):
    username: str = Field(..., max_length=10)
    email: EmailStr = Field(..., max_length=50)
    password: str = Field(..., max_length=128)

    @classmethod
    def hash_password(cls, value):
        if len(value) < 5:
            raise ValueError("Password must be at least 5 characters long")
        hashed_password = bcrypt.hashpw(value.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        return hashed_password


class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float


class ProductOut(BaseModel):
    id: int
    name: str
    description: str
    price: float

    class Config:
        from_attributes = True


class OrderCreate(BaseModel):
    user_id: int
    product_id: int


class OrderOut(BaseModel):
    id: int
    user_id: int
    product_id: int
    order_date: datetime
    status: str

    class Config:
        from_attributes = True



