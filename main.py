from flask import Flask, render_template
from dataalchemy.db_session import create_session, global_init
from dataalchemy.models import User, Role

app = Flask(__name__)
app.config['SECRET_KEY'] = 'crewdestruct'

global_init()

@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('Log_in.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('registration.html')

@app.route("/test_db")
def test_db():
    # создаём сессию для этого запроса
    db = create_session()
    try:
        # 1️⃣ Проверяем роль
        role = db.query(Role).filter(Role.name == "Student").first()
        if not role:
            role = Role(name="Student")
            db.add(role)
            db.commit()  # commit чтобы role.id появился

        # 2️⃣ Проверяем пользователя
        user = db.query(User).filter(User.email == "ivan@example.com").first()
        if not user:
            user = User(email="ivan@example.com", password="12345", balance=100.0, role=role)
            db.add(user)
            db.commit()  # commit сохраняет пользователя

        # 3️⃣ Выводим всех пользователей
        users = db.query(User).all()
        result = "<br>".join([f"{u.email} — {u.role.name} — {u.balance}" for u in users])
        return f"<h3>Пользователи в базе:</h3>{result}"

    except Exception as e:
        db.rollback()  # если ошибка, откат
        return f"Ошибка: {e}"
    finally:
        db.close()  # закрываем сессию

if __name__ == "__main__":
    app.run(debug=True)