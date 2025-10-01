from django.urls import path

from . import views

urlpatterns = [
    path('customer/', views.get_customers, name="get_customers"),
    path('customer/create/', views.create_customer, name="create_customer"),
    path('customer/<int:id>/', views.get_customer_by_id, name="get_customer_by_id"),
    path('customer/<int:id>/update/', views.update_customer, name="update_customer"),
    path('customer/<int:id>/delete/', views.delete_customer, name="delete_customer"),
    path('transaction/', views.get_transactions, name="get_transactions"),
    path('transaction/create/', views.create_transaction, name="create_transaction"),
    path('transaction/<int:id>/', views.get_transaction_by_id, name="get_transaction_by_id"),
    path('transaction/<int:id>/update/', views.update_transaction, name="update_transaction"),
    path('transaction/<int:id>/delete/', views.delete_transaction, name="delete_transaction"),
]