from flask import Blueprint, render_template
from flask import Flask, render_template, request, redirect
from models import db, Department, Employee
from crud import add_employee, get_employees, get_departments, get_department_by_name, update_average_salary, delete_employee_by_id, get_employee_by_id

departments = Blueprint("departments", __name__, template_folder='templates')


@departments.route('/')
def view_departments():
    departments_list = get_departments()
    for department in departments_list:
        update_average_salary(department.name)
    return render_template('department-list.html', departments=departments_list)