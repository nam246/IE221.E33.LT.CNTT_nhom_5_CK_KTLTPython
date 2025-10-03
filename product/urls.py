from django.urls import path

from product import views

urlpatterns = [
    path("", views.index, name="index"),
    path('category/', views.get_categories, name='category'),
    path('category/<int:category_id>/', views.get_category, name='category_by_id'),
    path('category/create', views.create_category, name='create_category'),
    path('products/', views.get_products, name="product"),
    path('products/<int:id>', views.get_product_by_id, name="product_detail"),
]
