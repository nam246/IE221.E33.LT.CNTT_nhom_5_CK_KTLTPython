from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from product.models import Product
from .models import Warehouse, InventoryItem
from .utils import warehouse_serializer, inventory_item_serializer


@login_required
@require_http_methods(['GET'])
def get_warehouses(request):
    warehouses = Warehouse.objects.all()
    data = [warehouse_serializer(w) for w in warehouses]
    return JsonResponse(data, safe=False)


@login_required
@require_http_methods(['GET'])
def get_warehouse_by_id(request, id):
    try:
        warehouse = Warehouse.objects.get(id=id)
        data = warehouse_serializer(warehouse)
        return JsonResponse(data)
    except Warehouse.DoesNotExist:
        return JsonResponse({'error': 'Warehouse not found'}, status=404)


@login_required
@csrf_exempt
@require_http_methods(['POST'])
def create_warehouse(request):
    name = request.POST.get('name')
    location = request.POST.get('location')
    if not name or not location:
        return JsonResponse({'error': 'Name and location are required'}, status=400)
    warehouse = Warehouse.objects.create(name=name, location=location)
    return JsonResponse(warehouse_serializer(warehouse), status=201)


@login_required
@csrf_exempt
@require_http_methods(['POST'])
def update_warehouse(request, id):
    try:
        warehouse = Warehouse.objects.get(id=id)
        name = request.POST.get('name')
        location = request.POST.get('location')
        if name:
            warehouse.name = name
        if location:
            warehouse.location = location
        warehouse.save()
        return JsonResponse(warehouse_serializer(warehouse))
    except Warehouse.DoesNotExist:
        return JsonResponse({'error': 'Warehouse not found'}, status=404)


@login_required
@csrf_exempt
@require_http_methods(['DELETE'])
def delete_warehouse(request, id):
    try:
        warehouse = Warehouse.objects.get(id=id)
        warehouse.delete()
        return JsonResponse({'message': 'Warehouse deleted successfully'})
    except Warehouse.DoesNotExist:
        return JsonResponse({'error': 'Warehouse not found'}, status=404)


@login_required
@require_http_methods(['GET'])
def get_inventory_items(request):
    items = InventoryItem.objects.all()
    data = [inventory_item_serializer(i) for i in items]
    return JsonResponse(data, safe=False)


@login_required
@require_http_methods(['GET'])
def get_inventory_item_by_id(request, id):
    try:
        item = InventoryItem.objects.get(id=id)
        data = inventory_item_serializer(item)
        return JsonResponse(data)
    except InventoryItem.DoesNotExist:
        return JsonResponse({'error': 'Inventory item not found'}, status=44)


@login_required
@csrf_exempt
@require_http_methods(['POST'])
def create_inventory_item(request):
    product_id = request.POST.get('product_id')
    warehouse_id = request.POST.get('warehouse_id')
    quantity = request.POST.get('quantity')

    if not all([product_id, warehouse_id, quantity]):
        return JsonResponse({'error': 'product_id, warehouse_id, and quantity are required'}, status=400)

    try:
        product = Product.objects.get(id=product_id)
        warehouse = Warehouse.objects.get(id=warehouse_id)
        item = InventoryItem.objects.create(product=product, warehouse=warehouse, quantity=quantity)
        return JsonResponse(inventory_item_serializer(item), status=201)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)
    except Warehouse.DoesNotExist:
        return JsonResponse({'error': 'Warehouse not found'}, status=404)


@login_required
@csrf_exempt
@require_http_methods(['POST'])
def update_inventory_item(request, id):
    try:
        item = InventoryItem.objects.get(id=id)
        quantity = request.POST.get('quantity')
        if quantity:
            item.quantity = quantity
            item.save()
        return JsonResponse(inventory_item_serializer(item))
    except InventoryItem.DoesNotExist:
        return JsonResponse({'error': 'Inventory item not found'}, status=404)


@login_required
@csrf_exempt
@require_http_methods(['DELETE'])
def delete_inventory_item(request, id):
    try:
        item = InventoryItem.objects.get(id=id)
        item.delete()
        return JsonResponse({'message': 'Inventory item deleted successfully'})
    except InventoryItem.DoesNotExist:
        return JsonResponse({'error': 'Inventory item not found'}, status=404)