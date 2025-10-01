import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from product_management.models import Category, Product


# Create your views here.


def index(request):
    return HttpResponse('this is product management page')


@login_required
@require_http_methods(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    data = []
    for category in categories:
        data.append({
            'name': category.name,
            'description': category.description,
        })

    return JsonResponse({'data': data}, safe=False, status=200)


def category_serializer(category):
    return {
        'id': category.id,
        'name': category.name,
    }


@login_required
@require_http_methods(['GET'])
def get_category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
        data = category_serializer(category)
        return JsonResponse({'data': data}, safe=False, status=200)
    except Category.DoesNotExist:
        return JsonResponse({'error': f'Category with id {category_id} not found'}, status=404)


@login_required
@require_http_methods(['POST'])
@csrf_exempt
def create_category(request):
    try:
        request_data = json.loads(request.body)
        Category.objects.create(request_data)
        return JsonResponse({'message': 'created successfully'}, safe=False, status=201)
    except Exception as error:
        return JsonResponse({'error': error}, status=400)


def product_serializer(product):
    return {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'quantity': product.quantity,
        'in_stock': product.in_stock,
        'category': product.category.id,
    }


@login_required
@require_http_methods(['GET'])
def get_products(request):
    try:
        products = Product.objects.all()
        data = []
        for product in products:
            data.append({
                'name': product.name,
                'description': product.description,
                'quantity': product.quantity,
                'in_stock': product.in_stock,
                'category': product.category.id,
            })

        return JsonResponse({'data': data}, safe=False, status=200)
    except Product.DoesNotExist:
        return JsonResponse({'error': f'Product with not found'}, status=404)


@login_required
@require_http_methods(['GET'])
def get_product_by_id(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        data = product_serializer(product)

        return JsonResponse({'data': data}, safe=False, status=200)
    except Product.DoesNotExist:
        return JsonResponse({'error': f'Product with id {product_id} not found'}, status=404)

@login_required
@require_http_methods(['POST'])
@csrf_exempt
def create_product(request):
    request_data = json.loads(request.body)
    Product.objects.create()

    return JsonResponse({'message': 'created successfully'}, safe=False, status=201)


@login_required
@require_http_methods(['GET'])
def get_product_by_cate(request, category_id):
    product = Product.objects.select_related('category').filter(id=category_id)
    data = product_serializer(product)
    return JsonResponse({'data': data}, safe=False, status=200)
