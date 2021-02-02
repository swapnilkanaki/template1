from django.db import models
from customer.models  import Customer

# Create your models here.

class Estimate(models.Model):
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    esti_date = models.CharField(max_length=30)
    due_date = models.CharField(max_length=30)
    esti_no = models.CharField(max_length=10)
    ref_no = models.CharField(max_length=10,null=True)
    #  / This fields store array data /
    items = models.CharField(max_length=33)     
    quantitys = models.CharField(max_length=33)     
    price = models.CharField(max_length=33)  
    discount = models.CharField(max_length=33,null=True)
    amount = models.CharField(max_length=33)     

    notes = models.CharField(max_length=50,null=True)
    subtotal = models.CharField(max_length=10)     
    tax = models.CharField(max_length=3,null=True)
    totalamount = models.CharField(max_length=10)     
    submitted_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:"estimate"
