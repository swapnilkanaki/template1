from django import forms
from .models import Product


unitlist=(
    ('Dr.  Mann', 'Dr.  Mann'),
    ('Mrs.  Goodwin', 'Mrs.  Goodwin'),
    ('Ernie Towne', 'Ernie Towne'),
    ('Charlotte III', 'Charlotte III'),
    ('Tre Johnson', 'Tre Johnson'),
    ('Malvina Batz', 'Malvina Batz'),
    (' Schmeler', ' Schmeler'),
    ('Freddy Ruecker', 'Freddy Ruecker'),
    ('mg', 'mg'),
    ('kg', 'kg'),
    ('in', 'in'),
) 

class AddProductForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'title': "Enter Product Name",'placeholder': "Product Name "}),label="Enter Product Name",max_length=20,min_length=2,required=True)   
    price=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'type':'number','title':"Product Price",'placeholder': "Product Price"}),label="Product Price",max_length=8,min_length=1,required=True)
    unit=forms.ChoiceField(widget=forms.Select(attrs={'class':"form-control","data-placeholder":"Unit ",'title': "select Unit"}),label="Unit ",choices=unitlist,required=True)
    description=forms.CharField(widget=forms.Textarea(attrs={'class':"form-control",'title': "Description",'placeholder': 'Description'}),label='Description',required=False)
 
    class Meta:
        model = Product
        fields = ('name','price','unit','description')
  