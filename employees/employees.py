import flask
from flask import Blueprint, render_template
from flask import Flask, render_template, request, redirect
from models import db, Department, Employee
from crud import add_employee, get_employees, get_departments, get_department_by_name, update_average_salary, delete_employee_by_id, get_employee_by_id

employees = Blueprint("employees", __name__, template_folder='templates')


@employees.route('/')
def index():
    """
    Shows page with the list of employees
    """
    return render_template('employee-list.html', employees=get_employees())


@employees.route('/create-employee', methods=['GET', 'POST'])
def create_employee():
    """Route for creating new employee.
    If the method is GET, the create page is rendered.
    If method is POST, redirects to home page"""
    if request.method == 'GET':
        return render_template('create-employee.html', departments=get_departments())

    if request.method == 'POST':
        print(request.form['birth_date'])
        add_employee(
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            birth_date=request.form['birth_date'],
            salary=request.form['salary'],
            department_name=request.form['department']
        )

    return redirect('/')


@employees.route('/<int:id>')
def employee_view(employee_id):
    employee = Employee.query.filter_by(id=employee_id).first()
    if employee:
        return render_template('employee-data.html', employee=employee)
    return f"Employee with {id=} does not exist"


@employees.route('/<int:employee_id>/delete', methods=['GET', 'POST'])
def delete_employee(employee_id):
    if request.method == 'POST':
        employee = delete_employee_by_id(employee_id)
        if employee:
            return redirect('/')
        flask.abort(404)
    return render_template('delete.html')


@employees.route('/<int:employee_id>/edit', methods=['GET', 'POST'])
def edit_employee(employee_id):
    employee = get_employee_by_id(employee_id)
    if request.method == 'POST':
        if employee:
            delete_employee_by_id(employee_id)
        add_employee(
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            birth_date=request.form['birth_date'],
            salary=request.form['salary'],
            department_name=request.form['department']
        )

        return redirect('/')
    return render_template('employee-update.html', employee=employee, departments=get_departments())