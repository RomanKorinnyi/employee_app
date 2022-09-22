from models import db, Department, Employee
from datetime import date


def add_employee(first_name: str, last_name: str, birth_date: str, salary: str, department_name: str):
    """
    Adds new employee to db
    :param first_name: str
    :param last_name: str
    :param birth_date: str
    :param salary: float
    :param department_name: str
    :return: class object
    """
    employee = Employee(
        first_name=first_name,
        last_name=last_name,
        birth_date=date.fromisoformat(birth_date),
        salary=salary,
        department_name=department_name)
    db.session.add(employee)
    db.session.commit()
    db.session.refresh(employee)
    return employee


def get_employees():
    return db.session.query(Employee).order_by(Employee.id).all()


def get_employee_by_id(employee_id):
    return db.session.query(Employee).filter_by(id=employee_id).first()


def delete_employee_by_id(employee_id):
    employee = get_employee_by_id(employee_id)
    if employee:
        db.session.delete(employee)
        db.session.commit()
        return employee


def get_departments():
    return db.session.query(Department).order_by(Department.id).all()


def get_department_by_id(department_id: int):
    return db.session.query(Department).get(department_id)


def get_department_by_name(department_name: str):
    return db.session.query(Department).filter_by(name=department_name).first()


def update_average_salary(department_name: str):
    employee_list = db.session.query(Employee).filter_by(department_name=department_name).all()
    department = db.session.query(Department).filter_by(name=department_name).first()
    if employee_list:
        average_sal = 0
        for emp in employee_list:
            average_sal += emp.salary
        department.average_salary = average_sal / len(employee_list)
    else:
        department.average_salary = 0
    db.session.commit()
    db.session.refresh(department)

    return department



