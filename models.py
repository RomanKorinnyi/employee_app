from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    average_salary = db.Column(db.Float(precision=2), nullable=True)
    employees = db.relationship('Employee')

    def __repr__(self):
        return '<Department {}>'.format(self.name)


class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    birth_date = db.Column(db.Date())
    salary = db.Column(db.Float(precision=2))
    department_name = db.Column(db.String(64), db.ForeignKey("departments.name"))

    def __repr__(self):
        return f'<Name {self.full_name}, ' \
               f'date {self.birth_date}, ' \
               f'salary {self.salary}, ' \
               f'department id {self.department_id} >'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(64))
