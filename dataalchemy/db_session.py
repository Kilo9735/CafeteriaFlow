from sqlalchemy.orm import sessionmaker, Session
from dataalchemy.db_engine import engine
from dataalchemy.models.base import Base

__factory = None  # фабрика сессий для многопоточности


def global_init():
    global __factory

    if __factory:  # если уже инициализирована, то пропускаем
        return

    __factory = sessionmaker(bind=engine, autoflush=False,
                             autocommit=False)  # создание фарбики при вызове
    Base.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    if not __factory:
        raise Exception("Фабрики нет, вызовите global_init()")
    return __factory()
