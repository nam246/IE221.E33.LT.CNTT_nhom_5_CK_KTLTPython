from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Customer, Transaction
from .utils import customer_serializer, transaction_serializer


@login_required
@require_http_methods(['POST'])
@csrf_exempt
def create_customer(request):
    """Create a new customer."""
    customer = Customer.objects.create(
        full_name=request.POST['full_name'],
        address=request.POST['address'],
        email=request.POST['email'],
        phone_number=request.POST['phone_number'],
        customer_type=request.POST['customer_type'],
    )
    return JsonResponse(customer_serializer(customer), status=201)


@login_required
@require_http_methods(['GET'])
def get_customers(request):
    """Get all customers."""
    customers = Customer.objects.all()
    data = [customer_serializer(customer) for customer in customers]
    return JsonResponse(data, safe=False)


@login_required
@require_http_methods(['GET'])
def get_customer_by_id(request, id):
    """Get customer by id."""
    customer = Customer.objects.get(id=id)
    return JsonResponse(customer_serializer(customer))


@login_required
@require_http_methods(['POST'])
@csrf_exempt
def update_customer(request, id):
    """Update customer by id."""
    customer = Customer.objects.get(id=id)
    customer.full_name = request.POST.get('full_name', customer.full_name)
    customer.address = request.POST.get('address', customer.address)
    customer.email = request.POST.get('email', customer.email)
    customer.phone_number = request.POST.get('phone_number', customer.phone_number)
    customer.customer_type = request.POST.get('customer_type', customer.customer_type)
    customer.save()
    return JsonResponse(customer_serializer(customer))


@login_required
@require_http_methods(['DELETE'])
@csrf_exempt
def delete_customer(request, id):
    """Delete customer by id."""
    customer = Customer.objects.get(id=id)
    customer.delete()
    return JsonResponse({'message': f'Successfully deleted customer id: {id}'}, status=202)


@login_required
@require_http_methods(['POST'])
@csrf_exempt
def create_transaction(request):
    """Create a new transaction."""
    customer = Customer.objects.get(id=request.POST['customer_id'])
    transaction = Transaction.objects.create(
        customer=customer,
        date=request.POST['date'],
        amount=request.POST['amount'],
        status=request.POST['status'],
        description=request.POST.get('description', ''),
    )
    return JsonResponse(transaction_serializer(transaction), status=201)


@login_required
@require_http_methods(['GET'])
def get_transactions(request):
    """Get all transactions."""
    transactions = Transaction.objects.all()
    data = [transaction_serializer(transaction) for transaction in transactions]
    return JsonResponse(data, safe=False)


@login_required
@require_http_methods(['GET'])
def get_transaction_by_id(request, id):
    """Get transaction by id."""
    transaction = Transaction.objects.get(id=id)
    return JsonResponse(transaction_serializer(transaction))


@login_required
@require_http_methods(['POST'])
@csrf_exempt
def update_transaction(request, id):
    """Update transaction by id."""
    transaction = Transaction.objects.get(id=id)
    transaction.date = request.POST.get('date', transaction.date)
    transaction.amount = request.POST.get('amount', transaction.amount)
    transaction.status = request.POST.get('status', transaction.status)
    transaction.description = request.POST.get('description', transaction.description)
    transaction.save()
    return JsonResponse(transaction_serializer(transaction))


@login_required
@require_http_methods(['DELETE'])
@csrf_exempt
def delete_transaction(request, id):
    """Delete transaction by id."""
    transaction = Transaction.objects.get(id=id)
    transaction.delete()
    return JsonResponse({'message': f'Successfully deleted transaction id: {id}'}, status=202)