
from base import BaseModel
from sqlalchemy import (
    Column,
    String,
    Integer,
)


class Student(BaseModel):
    __tablename__ = 'student'

    name = Column(String(200))
    age = Column(Integer)
