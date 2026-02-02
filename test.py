from dataalchemy.db_session import create_session, global_init
from dataalchemy.models import Role, User
from dataalchemy.models.base import Base
from dataalchemy.db_engine import engine

# Создаем таблицы (если еще не созданы)
Base.metadata.create_all(engine)

# Проверяем, есть ли роли, чтобы не дублировать
global_init()
session = create_session()
if session.query(Role).count() == 0:
    roles = [Role(name="Student"), Role(name="Cook"), Role(name="Admin")]
    session.add_all(roles)
    session.commit()
    print("Роли добавлены")
else:
    print("Роли уже есть")

# Берем роль Student для тестового пользователя
student_role = session.query(Role).filter_by(name="Student").first()

# Проверяем, есть ли тестовый пользователь
if session.query(User).filter_by(email="test@student.com").first() is None:
    test_user = User(
        email="test@student.com",
        password="12345",  # тестовый пароль
        balance=100.0,
        role=student_role
    )
    session.add(test_user)
    session.commit()
    print(f"Пользователь {test_user.email} добавлен с ролью {test_user.role.name}")
else:
    print("Тестовый пользователь уже существует")

# Выводим всех пользователей
users = session.query(User).all()
for u in users:
    print(f"{u.id}: {u.email}, роль: {u.role.name}, баланс: {u.balance}")
