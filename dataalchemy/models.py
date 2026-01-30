import sqlalchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from dataalchemy import Base, engine
from dataalchemy.db_session import session


class Role(Base):
    __tablename__ = 'roles'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String, unique=True)

    #связь с таблицей пользоватлей
    users = relationship("User", back_populates="role")


class User(Base):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True)
    password = sqlalchemy.Column(sqlalchemy.String)

    role_id = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey('roles.id'))

    #связь с таблтцей ролей
    role = relationship("Role", back_populates="users")

Base.metadata.create_all(engine)

#проверка
"""if __name__ == "__main__":
    # Создаём роли только если их ещё нет
    role_names = ["Ученик", "Повар", "Админ"]
    roles = []
    for name in role_names:
        role = session.query(Role).filter_by(name=name).first()
        if not role:
            role = Role(name=name)
            session.add(role)
            session.commit()
        roles.append(role)

    # Создаём пользователей только если их ещё нет
    test_users = [
        ("student@mail.com", "12345", "Ученик"),
        ("cook@mail.com", "12345", "Повар"),
        ("admin@mail.com", "12345", "Админ")
    ]

    for email, password, role_name in test_users:
        user = session.query(User).filter_by(email=email).first()
        if not user:
            role = session.query(Role).filter_by(name=role_name).first()
            user = User(email=email, password=password, role_id=role.id)
            session.add(user)
            session.commit()

    # Проверка: вывод всех пользователей и их ролей
    all_users = session.query(User).all()
    for user in all_users:
        print(f"{user.email} → {user.role.name}")"""