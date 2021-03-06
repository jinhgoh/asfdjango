from django.db import models

# Create your models here.

class InfectedPlace(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    lat = models.DecimalField(max_digits=20, decimal_places=16)
    lng = models.DecimalField(max_digits=20, decimal_places=16)
    happened_at = models.CharField(max_length=30, null=True, blank=True)
    reported2oie_at = models.DateTimeField(null=True, blank=True)
    memo = models.TextField(null=True, blank=True)
    password = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)