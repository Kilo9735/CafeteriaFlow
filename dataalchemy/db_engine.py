from sqlalchemy import create_engine
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # путь к файлу
db_dir = os.path.join(BASE_DIR, '..',
                      'database')  # database относительно dataalchemy
db_path = os.path.join(db_dir, 'school.db')

if not os.path.exists(db_dir):
    os.mkdir(db_dir)

engine = create_engine(f'sqlite:///{db_path}')
