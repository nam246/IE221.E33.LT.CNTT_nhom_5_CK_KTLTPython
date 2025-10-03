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

def employee_validator(data):
    """"""
    data['fullname'] = str(data['fullname'])
    data['email'] = str(data['email'])
    data['phone_number'] = str(data['phone_number'])
    data['position'] = str(data['position']) in ('Staff', 'Manager')
    data['department'] = data['department']
    data['net_salary'] = float(data['net_salary'])
    data['gross_salary'] = float(data['gross_salary'])

def employee_gross_salary_calc(net_salary, position):
    """Tính toán gross salary dựa vào net salary và position."""
    if position == 'staff':
        deduction_rate = 0.15
    else:  # manager
        deduction_rate = 0.20
    return net_salary / (1 - deduction_rate)
