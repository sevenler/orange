
from base import BaseModel
from sqlalchemy import (
    Column,
    String,
    Text,
)


class Major(BaseModel):
    __tablename__ = 'major'

    name = Column(String(200))
    description = Column(Text)
