import flask
from flask import Blueprint, render_template
from flask import Flask, render_template, request, redirect
from models import db, Department, Employee
from crud import add_employee, get_departments, update_average_salary, add_department, delete_department_by_id, get_department_by_id, update_department_name
from flask_login import login_required, current_user


departments = Blueprint("departments", __name__, template_folder='templates')


@departments.route('/', methods=['GET'])
@login_required
def view_departments():
    departments_list = get_departments()
    for department in departments_list:
        update_average_salary(department.name)
    return render_template('department-list.html', departments=departments_list, user=current_user)


@departments.route('/', methods=['POST'])
@login_required
def create_department():
    """Route creates new department.
        If the method is GET, the create page is rendered.
        If method is POST, redirects to home page"""
    if request.method == 'POST':
        add_department(
            department_name=request.form['department_name']
        )

    return redirect('/departments')


@departments.route('/<int:department_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_employee(department_id):
    if request.method == 'POST':
        department = delete_department_by_id(department_id)
        if department:
            return redirect('/departments')
        flask.abort(404)
    return render_template('delete.html', user=current_user)


@departments.route('/<int:department_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_department(department_id):
    department = get_department_by_id(department_id)
    if request.method == 'POST':
        if department:
            update_department_name(department_id, request.form['department_name'])

        return redirect('/departments')

    return render_template('department-update.html', department=department, user=current_user)
