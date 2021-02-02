from django import forms
from customer.models  import Customer
from .models import Estimate



class AddEstimateForm(forms.ModelForm):
    customer_id=forms.ModelChoiceField(widget=forms.Select(attrs={'class':"form-control","data-placeholder":" Customer ",'id':'customer_id','title': "select Customer"}),label="Customer",queryset=Customer.objects.all(),required=True)
    esti_date=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'id':'esti_date','title': "Estimate Date",'placeholder': "Estimate Date"}),label="Estimate Date",required=True)   
    due_date=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'id':'due_date','title': "Due Date",'placeholder': "Due Date"}),label="Due Date",required=True)   
   
    esti_no=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'title':"Estimate Number",'id':'esti_no','placeholder': "Estimate Number"}),label="Estimate Number",max_length=10,min_length=1,required=True)
    ref_no=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'title': "Referance Number",'id':'ref_no','placeholder': "Referance Number"}),label="Referance Number",max_length=10,min_length=1,required=False)   
    
    notes=forms.CharField(widget=forms.Textarea(attrs={'class':"form-control",'rows':2,'title': "Notes",'id':'notes','placeholder': 'Notes'}),label='Notes',max_length=50,min_length=2,required=False)
    subtotal=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'type':'number','id':'subtotal','onclick':'clasubtotal()','title':"Sub Total",'placeholder': "Sub Total"}),label="Sub Total",max_length=10,min_length=1,required=True)
    tax=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'type':'number','id':'tax','title':"tax",'placeholder': "Tax"}),label="Tax",max_length=10,min_length=1,required=False)
    totalamount=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'type':'number','id':'totalamount','title':"Total Amount",'placeholder': "Total Amount"}),label="Total Amount",max_length=10,min_length=1,required=True)
   
    class Meta:
        model = Estimate
        fields = ('customer_id','esti_date','due_date','esti_no','ref_no','notes','subtotal','tax','totalamount')
  