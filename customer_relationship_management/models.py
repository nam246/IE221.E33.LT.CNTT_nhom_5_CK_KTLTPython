from django.db import models


# Create your models here.

class Customer(models.Model):
    CUSTOMER_TYPES = [
        ('REGULAR', 'Regular Customer'),
        ('VIP', 'VIP Customer'),
        ('CORPORATE', 'Corporate Client'),
    ]
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=10,
        verbose_name="Phone Number"
    )
    customer_type = models.CharField(
        max_length=20,
        choices=CUSTOMER_TYPES,
        default='REGULAR',
        verbose_name="Customer Type"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class Transaction(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
        ('REFUNDED', 'Refunded'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.IntegerField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='COMPLETED',
        verbose_name="Status"
    )
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.full_name} - {self.amount} on {self.date}"
