import sqlalchemy
from sqlalchemy.orm import relationship
from .base import Base


class Dish(Base):

    __tablename__ = 'dishes'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String, unique=False)