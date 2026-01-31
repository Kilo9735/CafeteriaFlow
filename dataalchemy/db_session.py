from sqlalchemy.orm import sessionmaker
from dataalchemy.db_engine import engine

Session = sessionmaker(bind=engine)
session = Session()  # глобальная сессия для всей работы с бд
