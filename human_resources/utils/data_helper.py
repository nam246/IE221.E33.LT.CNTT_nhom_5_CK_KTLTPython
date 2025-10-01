import random
from datetime import datetime


def department_serializer(department):
    """serialize a department"""
    return {
        "id": department.id,
        "name": department.name,
    }


def employee_code_generator(position):
    now = datetime.now()
    prefix = 'sf' if position == 'Staff' else 'mg' if position == 'Manager' else None
    random_number = random.randint(100, 999)
    code = prefix + str(random_number) + now.strftime("%Y%m%d")

    return code


def employee_serializer(employee):
    return {
        'id': employee.id,
        'employee_code': employee.employee_code,
        'fullname': employee.fullname,
        'address': employee.address,
        'email': employee.email,
        'phone_number': employee.phone_number,
        'department': employee.department_id,
        'net_salary': employee.net_salary,
        'gross_salary': employee.gross_salary
    }


def employee_gross_salary_calc(employee):
    """"""
