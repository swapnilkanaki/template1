from django import forms
from .models import Customer


crcy=(
    ('India Rupee', 'India Rupee INR ₹'),
    ('Albania Lek', 'Albania Lek ALL Lek'),
    ('Afghanistan ', 'Afghanistan  AFN ؋'),
    ('Argentina Peso', 'Argentina Peso 	ARS	$'),
    ('Aruba Guilder', 'Aruba Guilder 	AWG	ƒ'),
    ('Australia Dollar', 'Australia Dollar  AUD	$'),
    ('Azerbaijan Manat', 'Azerbaijan Manat  AZN ₼'),
    ('Bahamas Dollar', 'Bahamas Dollar  BSD $'),
    ('Barbados Dollar', 'Barbados Dollar BBD $'),
    ('Belarus Ruble', 'Belarus Ruble  BYN	Br'),
    ('Belize Dollar', 'Belize Dollar BZD BZ$'),
    ('Bermuda Dollar', 'Bermuda Dollar BMD $'),
    ('Bolivia Bolíviano', 'Bolivia  BOB $b'),
    
) 
billcountry=(
    ('India', 'India'),
    ('Afghanistan', 'Afghanistan'),
    ('Albania', 'Albania'),
    ('Algeria', 'Algeria'),
    ('Andorra', 'Andorra'),
    ('Angola', 'Angola'),
    ('Antigua ', 'Antigua'),
    ('Argentina', 'Argentina'),
    ('Armenia', 'Armenia'),
    ('Australia', 'Australia'),
) 
class AddCustomerForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'title': "Enter Customer fullname",'placeholder': "Customer Name "}),label="Customer Name",max_length=30,min_length=2,required=True)   
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':"form-control",'title': "Enter Customer Email",'placeholder': "Email"}),label="Customer Email",max_length=30,min_length=4,required=True) 
    currency=forms.ChoiceField(widget=forms.Select(attrs={'class':"form-control","data-placeholder":"Currency Type",'title': "select Currency Type"}),label="Currency Type",choices=crcy,required=False)
    contact_name=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'title': "Enter Contact Name",'placeholder': "Contact-Name"}),label="Contact-Name",max_length=20,min_length=3,required=False)  
    phone=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'type':'number','title':"Customer mobile number",'placeholder': "Customer Mobile"}),label="Customer Mobile",max_length=10,min_length=10)
    website=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'title':"Websiter",'placeholder': "http://......"}),label="website",max_length=30,min_length=5,required=False)
    bill_name=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'id':"bill_name",'title': "Enter Billing Name",'placeholder': "Enter Billing Name"}),label="Enter Billing Name",max_length=30,min_length=3,required=False)  
    bill_state=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'id':"bill_state",'title': "Enter State Name",'placeholder': "Enter State Name"}),label="Enter State Name",max_length=10,min_length=3,required=False)  
    bill_address1=forms.CharField(widget=forms.Textarea(attrs={'class':"form-control",'id':"bill_address1",'rows':2,'title': "Enter Billing Address",'placeholder': 'Address...1'}),label='Billing Address',max_length=40,min_length=2,required=False)
    bill_address2=forms.CharField(widget=forms.Textarea(attrs={'class':"form-control",'id':"bill_address2",'title': "Enter Billing Address",'rows':1,'placeholder': 'Address...2'}),label='Billing Address',max_length=40,min_length=2,required=False)
    bill_country=forms.ChoiceField(widget=forms.Select(attrs={'class':"form-control",'id':"bill_country","data-placeholder":"Country Name",'title': "select Country Name"}),label="Country Name",choices=billcountry,required=False)
    bill_city=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'id':"bill_city",'title': "Enter City Name",'placeholder': "Enter City Name"}),label="Enter City Name",max_length=10,min_length=3,required=False)  
    bill_phone=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'id':"bill_phone",'type':'number','title':"Billing mobile number",'placeholder': "Billing Mobile"}),label="Billing Mobile",max_length=10,min_length=10,required=False)
    bill_zipcode=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'id':"bill_zipcode",'title': "Enter Zip Code",'placeholder': "Enter Zip Code"}),label="Enter Zip Code",max_length=8,min_length=3,required=False)  
    shipp_name=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'id':"shipp_name",'title': "Enter Shipping Name",'placeholder': "Enter Shipping Name"}),label="Enter Shipping Name",max_length=30,min_length=3,required=False)  
    shipp_state=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'id':"shipp_state",'title': "Enter State Name",'placeholder': "Enter State Name"}),label="Enter State Name",max_length=10,min_length=3,required=False)  
    shipp_address1=forms.CharField(widget=forms.Textarea(attrs={'class':"form-control",'id':"shipp_address1",'rows':2,'title': "Enter Shipping Address",'placeholder': 'Address...1'}),label='Shipping Address',max_length=40,min_length=2,required=False)
    shipp_address2=forms.CharField(widget=forms.Textarea(attrs={'class':"form-control",'id':"shipp_address2",'rows':1,'title': "Enter Shipping Address",'placeholder': 'Address...2'}),label='Shipping Address',max_length=40,min_length=2,required=False)
    shipp_country=forms.ChoiceField(widget=forms.Select(attrs={'class':"form-control",'id':"shipp_country","data-placeholder":"Country Name",'title': "select Country Name"}),label="Country Name",choices=billcountry,required=False)
    shipp_city=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'id':"shipp_city",'title': "Enter City Name",'placeholder': "Enter City Name"}),label="Enter City Name",max_length=10,min_length=3,required=False)  
    shipp_phone=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'id':"shipp_phone",'type':'number','title':"Shipping mobile number",'placeholder': "Shipping Mobile"}),label="Shipping Mobile",max_length=10,min_length=10,required=False)
    shipp_zipcode=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'id':"shipp_zipcode",'title': "Enter Zip Code",'placeholder': "Enter Zip Code"}),label="Enter Zip Code",max_length=8,min_length=3,required=False) 
    
    class Meta:
        model = Customer
        fields = ('name','email','currency','contact_name','phone','website','bill_name','bill_state','bill_address1','bill_address2',
        'bill_country','bill_city','bill_phone','bill_zipcode','shipp_name','shipp_state','shipp_address1','shipp_address2','shipp_country','shipp_city'
        ,'shipp_phone','shipp_zipcode')
  