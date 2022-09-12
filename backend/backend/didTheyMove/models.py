from django.db import models
from django.utils import timezone
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
# Create your models here.

STATUS = [
    ('For Sale','For Sale'),
    ('For Rent','For Rent'),
    ('Recently Sold (6)','Recently Sold (6)'),
    ('Recently Sold (12)','Recently Sold (12)'),
    ('Off Market', 'Off Market'),
    ('No Change', 'No Change')
]

class DidTheyMove(models.Model):
    customer = models.CharField(max_length=120)
    address = models.TextField()
    zipCode = models.TextField()
    phoneNumber = models.CharField(max_length=20)
    client = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS, default='No Change')
    soldSinceDate = models.BooleanField(default=True)

    def _str_(self):
        return self.customer

# class ClientList(models.Model):
#     client = models.CharField()
#     list = models.FileField()

class ZipCodes(models.Model):
    lastChecked = models.DateField(default=date.today)
    zipCode = models.IntegerField()

class HomeData(models.Model):
    address = models.TextField()
    zipCode = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS, default='Off Market')
    listDate = models.DateField(blank=True)
    property_id = models.CharField(max_length=12)

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(('admin'), default=False)
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

# class Customer(models.Model):
#     name = models.CharField(max_length=20)
    # accessToken = models.