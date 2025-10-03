from django.urls import path
from . import views

urlpatterns = [
    path('warehouses/', views.get_warehouses, name='get_warehouses'),
    path('warehouses/<int:id>/', views.get_warehouse_by_id, name='get_warehouse_by_id'),
    path('warehouses/create/', views.create_warehouse, name='create_warehouse'),
    path('warehouses/<int:id>/update/', views.update_warehouse, name='update_warehouse'),
    path('warehouses/<int:id>/delete/', views.delete_warehouse, name='delete_warehouse'),
    path('inventory-items/', views.get_inventory_items, name='get_inventory_items'),
    path('inventory-items/<int:id>/', views.get_inventory_item_by_id, name='get_inventory_item_by_id'),
    path('inventory-items/create/', views.create_inventory_item, name='create_inventory_item'),
    path('inventory-items/<int:id>/update/', views.update_inventory_item, name='update_inventory_item'),
    path('inventory-items/<int:id>/delete/', views.delete_inventory_item, name='delete_inventory_item'),
]
