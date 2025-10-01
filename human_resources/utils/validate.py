def employee_validator(data):
    """"""
    data['fullname'] = str(data['fullname'])
    data['email'] = str(data['email'])
    data['phone_number'] = str(data['phone_number'])
    data['position'] = str(data['position']) in ('Staff', 'Manager')
    data['department'] = data['department']
    data['net_salary'] = float(data['net_salary'])
    data['gross_salary'] = float(data['gross_salary'])

