import flask
from flask import Flask, render_template, request, redirect
from models import db, User
from crud import add_employee, get_employees, get_departments, get_department_by_name, update_average_salary, delete_employee_by_id, get_employee_by_id
from departments import departments
from employees import employees
from authenticate import auth
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = 'password'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['DEBUG_MODE'] = True
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


app.register_blueprint(departments.departments, url_prefix='/departments')
app.register_blueprint(employees.employees, url_prefix='')
app.register_blueprint(auth.auth, url_prefix='/')


@app.before_first_request
def create_table():
    db.create_all()


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
