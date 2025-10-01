def customer_serializer(customer):
    """Serialize a customer object."""
    return {
        'id': customer.id,
        'full_name': customer.full_name,
        'address': customer.address,
        'email': customer.email,
        'phone_number': customer.phone_number,
        'customer_type': customer.customer_type,
        'created_at': customer.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        'updated_at': customer.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
    }


def transaction_serializer(transaction):
    """Serialize a transaction object."""
    return {
        'id': transaction.id,
        'customer_id': transaction.customer.id,
        'date': transaction.date,
        'amount': transaction.amount,
        'status': transaction.status,
        'description': transaction.description,
        'created_at': transaction.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        'updated_at': transaction.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
    }
