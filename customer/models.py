from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    currency = models.CharField(max_length=20)
    contact_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10,null=True)
    website = models.CharField(max_length=30,null=True)
    bill_name = models.CharField(max_length=25,null=True)
    bill_state = models.CharField(max_length=10,null=True)
    bill_address1 = models.CharField(max_length=40,null=True)
    bill_address2 = models.CharField(max_length=40,null=True)
    bill_country = models.CharField(max_length=10,null=True)
    bill_city = models.CharField(max_length=10,null=True)
    bill_phone = models.CharField(max_length=10,null=True)
    bill_zipcode = models.CharField(max_length=8,null=True)
    shipp_name = models.CharField(max_length=25,null=True)
    shipp_state = models.CharField(max_length=10,null=True)
    shipp_address1 = models.CharField(max_length=40,null=True)
    shipp_address2 = models.CharField(max_length=40,null=True)
    shipp_country = models.CharField(max_length=10,null=True)
    shipp_city = models.CharField(max_length=10,null=True)
    shipp_phone = models.CharField(max_length=10,null=True)
    shipp_zipcode = models.CharField(max_length=8,null=True)
    submitted_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:"customer"
    def __str__(self):
        f=str(self.id)+" "+self.name
        return f

