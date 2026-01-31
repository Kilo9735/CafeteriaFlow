import sqlalchemy
from sqlalchemy.orm import relationship
from .base import Base


class User(Base):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True)
    password = sqlalchemy.Column(sqlalchemy.String)

    balance = sqlalchemy.Column(sqlalchemy.Float, default=0.0)

    role_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey('roles.id'))

    # связь с таблтцей ролей
    role = relationship("Role", back_populates="users")
