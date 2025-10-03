from django.db import models

from human_resources.utils import employee_gross_salary_calc


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
    gross_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.gross_salary = employee_gross_salary_calc(self.net_salary, self.position)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.fullname + ' ' + self.employee_code
