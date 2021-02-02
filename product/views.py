from django.shortcuts import render , HttpResponseRedirect
from .forms import AddProductForm
from .models import Product
from django.contrib.auth.models import auth
from django.contrib import messages

# Create your views here.

# This views for Add New Product.
def Product_addProduct(request):
    if request.session.has_key('user'):
        if request.method == 'POST':
            Product_Form = AddProductForm(request.POST)
            if Product_Form.is_valid():
                name = Product_Form.cleaned_data['name']
                price = Product_Form.cleaned_data['price']
                unit = Product_Form.cleaned_data['unit']
                description = Product_Form.cleaned_data['description']
                Product_obj = Product(name=name, price=price, unit=unit, description=description)
                Product_obj.save()
                Product_Form = AddProductForm()
                messages.success(request, 'Product Added Successfully!')
                return HttpResponseRedirect('/Product_viewProduct')
        else:
            Product_Form = AddProductForm()
        return render(request , 'product/add_product.html', {'form':Product_Form})
    else:
        return redirect('/login') 

# This views for Product List / Product Home page.
def Product_viewProduct(request):
    if request.session.has_key('user'):
        return render(request , 'product/product_home.html' , {'product':Product.objects.all()})
    else:
        return HttpResponseRedirect("/login")


# This views for Delete Particular Product.
def Product_deleteProduct(request ,id):
    if request.session.has_key('user'):
        if request.method == 'POST':
            pi = Product.objects.get(pk=id)
            print("\n \n  delete product ")
            pi.delete()
            messages.success(request, 'Product Deleted Successfully!')
            return HttpResponseRedirect('/Product_viewProduct')
    else:
        return HttpResponseRedirect("/login")   


# This views for Update Product Data.
def Product_updateProduct(request ,id):
    if request.session.has_key('user'):
        if request.method == 'POST':
            pi = Product.objects.get(pk=id)
            product_form = AddProductForm(request.POST, instance=pi)
            if product_form.is_valid():
                product_form.save()
                messages.success(request, 'Product Updated Successfully!')
                return HttpResponseRedirect('/Product_viewProduct')
        else:
            pi = Product.objects.get(pk=id)
            product_form = AddProductForm(instance=pi)
        return render(request , 'product/add_product.html', {'form':product_form})
    else:
        return HttpResponseRedirect("/login")     