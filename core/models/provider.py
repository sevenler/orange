
from base import BaseModel
from sqlalchemy import (
    Column,
    String,
)


class Provider(BaseModel):
    __tablename__ = 'provider'

    name = Column(String(200))
    code = Column(String(100))
