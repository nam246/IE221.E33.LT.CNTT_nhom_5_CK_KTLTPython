def warehouse_serializer(warehouse):
    return {
        'id': warehouse.id,
        'name': warehouse.name,
        'location': warehouse.location
    }

def inventory_item_serializer(item):
    return {
        'id': item.id,
        'product': item.product.id,
        'product_name': item.product.name,
        'warehouse': item.warehouse.id,
        'warehouse_name': item.warehouse.name,
        'quantity': item.quantity
    }
