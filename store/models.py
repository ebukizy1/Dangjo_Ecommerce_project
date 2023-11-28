from django.db import models

# Create your models here.
from uuid import uuid4

from django.db import models
from django.conf import settings


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey('Collection', on_delete=models.CASCADE, related_name='products')


class Collection(models.Model):
    title = models.CharField(max_length=225)
    featured_product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='+')


class Customer(models.Model):
    MEMBERSHIP_CHOICE = [
        ('M', 'GOLD'),
        ('B', 'BRONZE'),
        ('S', 'SILVER'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)


class Cart(models.Model):
    create_at = models.DateTimeField(auto_now=True)


class CartItem(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)


class Order(models.Model):
    PAYMENT_CHOICES = [
        ('P',  'PENDING'),
        ('C',  'COMPLETED'),
        ('F', 'FAILED')
    ]
    order_id = models.UUIDField(default=uuid4, primary_key=True)
    Place_at = models.DateTimeField(auto_now=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_CHOICES, default='P')
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    unity_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    house_number = models.PositiveIntegerField()
    street_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
