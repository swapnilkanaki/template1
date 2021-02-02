from django.shortcuts import render , HttpResponseRedirect
from .forms import AddCustomerForm
from .models import Customer
from django.contrib.auth.models import auth
from django.contrib import messages


# This views for Add New Customer.
def Customer_addCustomer(request):
    if request.session.has_key('user'):
        if request.method == 'POST':
            Customer_Form = AddCustomerForm(request.POST)
            if Customer_Form.is_valid():
                name = Customer_Form.cleaned_data['name']
                email = Customer_Form.cleaned_data['email']
                currency = Customer_Form.cleaned_data['currency']
                contact_name = Customer_Form.cleaned_data['contact_name']
                phone = Customer_Form.cleaned_data['phone']
                website = Customer_Form.cleaned_data['website']
                bill_name = Customer_Form.cleaned_data['bill_name']
                bill_state = Customer_Form.cleaned_data['bill_state']
                bill_address1 = Customer_Form.cleaned_data['bill_address1']
                bill_address2 = Customer_Form.cleaned_data['bill_address2']
                bill_country = Customer_Form.cleaned_data['bill_country']
                bill_city = Customer_Form.cleaned_data['bill_city']
                bill_phone = Customer_Form.cleaned_data['bill_phone']
                bill_zipcode = Customer_Form.cleaned_data['bill_zipcode']
                shipp_name = Customer_Form.cleaned_data['shipp_name']
                shipp_state = Customer_Form.cleaned_data['shipp_state']
                shipp_address1 = Customer_Form.cleaned_data['shipp_address1']
                shipp_address2 = Customer_Form.cleaned_data['shipp_address2']
                shipp_country = Customer_Form.cleaned_data['shipp_country']
                shipp_city = Customer_Form.cleaned_data['shipp_city']
                shipp_phone = Customer_Form.cleaned_data['shipp_phone']
                shipp_zipcode = Customer_Form.cleaned_data['shipp_zipcode']
                Cust_obj = Customer(name=name, email=email, currency=currency,
                 contact_name=contact_name,phone=phone,website=website,
                 bill_name=bill_name,bill_state=bill_state,bill_address1=bill_address1,
                 bill_address2=bill_address2,bill_country=bill_country,bill_city=bill_city,
                 bill_phone=bill_phone,bill_zipcode=bill_zipcode,shipp_name=shipp_name,
                 shipp_state=shipp_state,shipp_address1=shipp_address1,shipp_address2=shipp_address2,
                 shipp_country=shipp_country,shipp_city=shipp_city,shipp_phone=shipp_phone,
                 shipp_zipcode=shipp_zipcode)
                Cust_obj.save()
                Customer_Form = AddCustomerForm()
                messages.success(request, 'Customer Added Successfully!')
                return HttpResponseRedirect('/Customer_viewCustomer')
        else:
            Customer_Form = AddCustomerForm()
        return render(request , 'customer/add_customer.html', {'form':Customer_Form})
    else:
        return redirect('/login') 



# This views for Customer List / Customer Home page.
def Customer_viewCustomer(request):
    if request.session.has_key('user'):
        return render(request , 'customer/customer_home.html' , {'customer':Customer.objects.all()})
    else:
        return HttpResponseRedirect("/login")




# This views for Delete Particular Customer.
def Customer_deleteCustomer(request ,id):
    if request.session.has_key('user'):
        if request.method == 'POST':
            pi = Customer.objects.get(pk=id)
            pi.delete()
            messages.success(request, 'Customer Deleted Successfully!')
            return HttpResponseRedirect('/Customer_viewCustomer')
    else:
        return HttpResponseRedirect("/login")



# This views for Update Customer Data.
def Customer_updateCustomer(request ,id):
    if request.session.has_key('user'):
        if request.method == 'POST':
            pi = Customer.objects.get(pk=id)
            customer_form = AddCustomerForm(request.POST, instance=pi)
            if customer_form.is_valid():
                customer_form.save()
                messages.success(request, 'Customer Updated Successfully!')
                return HttpResponseRedirect('/Customer_viewCustomer')
        else:
            pi = Customer.objects.get(pk=id)
            customer_form = AddCustomerForm(instance=pi)
        return render(request , 'customer/add_customer.html', {'form':customer_form})
    else:
        return HttpResponseRedirect("/login")




