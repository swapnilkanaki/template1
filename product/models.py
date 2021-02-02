from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.CharField(max_length=8)
    unit = models.CharField(max_length=16)
    description = models.CharField(max_length=20,null=True)
    submitted_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:"product"