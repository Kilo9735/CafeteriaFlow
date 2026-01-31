import sqlalchemy
from sqlalchemy.orm import relationship
from .base import Base


class Role(Base):
    __tablename__ = 'roles'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String, unique=True)

    #связь с таблицей пользоватлей
    users = relationship("User", back_populates="role")
