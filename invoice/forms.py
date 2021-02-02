from django import forms
from customer.models  import Customer
from .models import Invoice



class AddInvoiceForm(forms.ModelForm):
    customer_id=forms.ModelChoiceField(widget=forms.Select(attrs={'class':"form-control","data-placeholder":" Customer ",'id':'customer_id','title': "select Customer"}),label="Customer",queryset=Customer.objects.all(),required=True)
    inv_date=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'id':'inv_date','title': "invoice Date",'placeholder': "invoice Date"}),label="invoice Date",required=True)   
    due_date=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'id':'due_date','title': "Due Date",'placeholder': "Due Date"}),label="Due Date",required=True)   
   
    inv_no=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'title':"invoice Number",'id':'inv_no','placeholder': "invoice Number"}),label="invoice Number",max_length=10,min_length=1,required=True)
    ref_no=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'title': "Referance Number",'id':'ref_no','placeholder': "Referance Number"}),label="Referance Number",max_length=10,min_length=1,required=False)   
    
    notes=forms.CharField(widget=forms.Textarea(attrs={'class':"form-control",'rows':2,'title': "Notes",'id':'notes','placeholder': 'Notes'}),label='Notes',max_length=50,min_length=2,required=False)
    subtotal=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'type':'number','id':'subtotal','onclick':'clasubtotal()','title':"Sub Total",'placeholder': "Sub Total"}),label="Sub Total",max_length=10,min_length=1,required=True)
    tax=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'type':'number','id':'tax','title':"tax",'placeholder': "Tax"}),label="Tax",max_length=10,min_length=1,required=False)
    totalamount=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'type':'number','id':'totalamount','title':"Total Amount",'placeholder': "Total Amount"}),label="Total Amount",max_length=10,min_length=1,required=True)
   
    class Meta:
        model = Invoice
        fields = ('customer_id','inv_date','due_date','inv_no','ref_no','notes','subtotal','tax','totalamount')
  