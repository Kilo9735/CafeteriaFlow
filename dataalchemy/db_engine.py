from sqlalchemy import create_engine
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, '..', 'database')
DB_PATH = os.path.join(DB_DIR, 'school.db')

if not os.path.exists(DB_DIR):
    os.mkdir(DB_DIR)

# движок для SQLite
engine = create_engine(f'sqlite:///{DB_PATH}?check_same_thread=False')
