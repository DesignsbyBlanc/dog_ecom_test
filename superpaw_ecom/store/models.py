from email.policy import default
from django.db import models
import datetime
# Create your models here

# Categories of products


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

# Customers


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

# All of our products


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(
        max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True,)
    phone = models.CharField(max_length=20, blank=True, default='')
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.product


# Model for auth token reqeust

# class AuthToken(models.Model):
#     auth_token = models.CharField(max_length=200)
#     created_at = models.DateTimeField(auto_now_add=True)
#     expires_on = models.DateTimeField() # Needs equation that adds 1 hour to the <created_at> field
#     is_expired = models.BooleanField(default=False) # Needs to logic to set this to true when <expires_on> field is true

# class RefreshToken(models.Model):
#     refresh_token = models.CharField(max_length=200)
#     created_at = models.DateTimeField(auto_now_add=True)
#     expires_on = models.DateTimeField()
#     is_expired = models.BooleanField(default=False)
