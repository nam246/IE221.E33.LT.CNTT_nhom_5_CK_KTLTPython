from django.db import models


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    POSITION_CHOICES = [
        ('staff', 'Staff'),
        ('manager', 'Manager'),
    ]
    employee_code = models.CharField(max_length=10)
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.TextField()
    position = models.CharField(max_length=100, choices=POSITION_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department')
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)
    gross_salary = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname + ' ' + self.address + ' ' + self.email + ' ' + self.phone_number + ' ' + self.position
