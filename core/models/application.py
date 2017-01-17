from base import BaseModel
from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime,
)


class Application(BaseModel):
    __tablename__ = 'application'

    name = Column(String(200))
    status = Column(Integer)
    apply_time = Column(DateTime)
    apply_student = Column(Integer)
