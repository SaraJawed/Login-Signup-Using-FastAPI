#This file is creating a User model for a database using SQLAlchemy

from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base # It’s the "starting point" that helps us create tables.

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)


