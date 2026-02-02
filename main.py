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



if __name__ == "__main__":
    app.run(debug=True)