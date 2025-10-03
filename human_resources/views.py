from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .utils import employee_code_generator, employee_serializer, department_serializer, employee_validator
from .models import Department, Employee


# Create your views here.

def index(request):
    return HttpResponse('this is human resource page')


@login_required
@require_http_methods(['POST'])
@csrf_exempt
def create_department(request):
    """create a new department"""
    department = Department.objects.create(name=request.POST['name'])
    return JsonResponse(department_serializer(department), status=201)


@login_required
@require_http_methods(['GET'])
def get_departments(request):
    """Get all departments"""
    departments = Department.objects.all()
    data = []
    for department in departments:
        data.append(department_serializer(department))
    return JsonResponse(data, safe=False)


@login_required
@require_http_methods(['GET'])
def get_department_employees(request, id):
    """Get all department employees"""
    department = Department.objects.get(id=id)
    employees = Employee.objects.filter(department=department)
    data = []
    for employee in employees:
        data.append(employee_serializer(employee))
    return JsonResponse({'data': data}, safe=False, status=200)


@login_required
@require_http_methods(['GET'])
def get_department_by_id(request, department_id):
    """get department by id"""
    department = Department.objects.get(id=department_id)
    data = department_serializer(department)
    return JsonResponse({'data': data}, safe=False, status=200)


@login_required
@require_http_methods(['POST'])
@csrf_exempt
def create_employee(request):
    """create a new employee"""
    data = {
        'employee_code': employee_code_generator(request.POST['position']),
        'fullname': request.POST['fullname'],
        'address': request.POST['address'],
        'email': request.POST['email'],
        'phone_number': request.POST['phone_number'],
        'position': request.POST['position'],
        'department': Department.objects.get(id=request.POST['department']),
        'net_salary': request.POST['net_salary'],
    }

    employee_validator(data)

    Employee.objects.create(
        employee_code=data['employee_code'],
        fullname=data['fullname'],
        address=data['address'],
        email=data['email'],
        phone_number=data['phone_number'],
        position=data['position'],
        department=data['department'],
        net_salary=data['net_salary'],
    )

    return JsonResponse({"message": "created successfully"}, safe=False, status=201)


@login_required
@require_http_methods(['GET'])
def get_employees(request):
    """Get all employees"""
    employees = Employee.objects.all()
    data = []
    for employee in employees:
        data.append(employee_serializer(employee))
    return JsonResponse({'data': data}, safe=False, status=200)


@login_required
@require_http_methods(['GET'])
def get_employee_by_id(request, id):
    """get employee by id"""
    if Employee.objects.filter(id=id).exists():
        employee = Employee.objects.get(id=id)
        data = employee_serializer(employee)
        return JsonResponse({'data': data}, safe=False, status=200)
    else:
        return JsonResponse({"message": "employee not found"}, safe=False, status=200)


@login_required
@require_http_methods(['DELETE'])
@csrf_exempt
def delete(request, id):
    """delete employee by id"""
    if Employee.objects.filter(id=id).exists():
        employee = Employee.objects.get(id=id)
        res = employee.delete()
        return JsonResponse({'message': 'success deleted employee id: ' + str(id)}, safe=False, status=202)
    else:
        return JsonResponse({"message": "employee not found"}, safe=False, status=200)


@login_required
@require_http_methods(['POST'])
@csrf_exempt
def update(request, id):
    """update employee by id"""
    if Employee.objects.filter(id=id).exists():
        edit_employee = Employee.objects.filter(id=id).update(
            fullname=request.POST['fullname'],
            address=request.POST['address'],
            email=request.POST['email'],
            phone_number=request.POST['phone_number'],
            position=request.POST['position'],
            department=request.POST['department'],
            net_salary=request.POST['net_salary'],
        )
        return JsonResponse({'data': edit_employee, "message": "updated successfully"}, safe=False, status=203)
    else:
        return JsonResponse({"message": "employee not found"}, safe=False, status=404)
