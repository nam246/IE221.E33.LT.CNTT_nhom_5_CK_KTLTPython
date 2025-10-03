from django.urls import path

from human_resources import views

urlpatterns = [
    path("", views.index, name="index"),
    path('department/', views.get_departments, name="department"),
    path('department/create/', views.create_department, name="department_create"),
    path('department/<int:id>/', views.get_department_by_id, name="department_detail"),
    path('department/<int:id>/employees/', views.get_department_employees, name="department_employees"),
    path('employee/', views.get_employees, name="employee"),
    path("employee/<int:id>/", views.get_employee_by_id, name="employee_detail"),
    path("employee/create/", views.create_employee, name="employee_create"),
    path("employee/<int:id>/delete/", views.delete, name="employee_delete"),
    path("employee/<int:id>/update/", views.update, name="employee_update"),
]
