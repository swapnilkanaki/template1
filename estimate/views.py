from django.shortcuts import render , HttpResponseRedirect
from .forms import AddEstimateForm
from .models import Estimate
from django.contrib.auth.models import auth
from django.contrib import messages
from product.models import Product


# Create your views here.

# This views for Add New Product.
def Estimate_addEstimate(request):
    if request.session.has_key('user'):
        if request.method == 'POST':
            Estimate_Form = AddEstimateForm(request.POST)
            if Estimate_Form.is_valid():
                customer_id = Estimate_Form.cleaned_data['customer_id']
                esti_date = Estimate_Form.cleaned_data['esti_date']
                due_date = Estimate_Form.cleaned_data['due_date']
                esti_no = Estimate_Form.cleaned_data['esti_no']
                ref_no = Estimate_Form.cleaned_data['ref_no']
                notes = Estimate_Form.cleaned_data['notes']
                subtotal = Estimate_Form.cleaned_data['subtotal']
                tax = Estimate_Form.cleaned_data['tax']
                totalamount = Estimate_Form.cleaned_data['totalamount']

                if request.POST['update'] =="True":
                    Estimate_obj = Estimate(customer_id=customer_id, esti_date=esti_date, due_date=due_date, esti_no=esti_no
                    , ref_no=ref_no, notes=notes, subtotal=subtotal, tax=tax, totalamount=totalamount)
                    Estimate_obj.save()
                    Estimate_Form = AddEstimateForm()
                    messages.success(request, 'Estimate Added Successfully!')
                    return HttpResponseRedirect('/Estimate_viewEstimate')

                ## Array reading
                items = request.POST['itm0']
                quantitys = request.POST['itemquantity0']
                price = request.POST['priceitem0']
                discount = request.POST['itemdiscount0']
                amount = request.POST['itemamount0']
                print(items)
                coun =int(request.POST['coun'])
                if coun > 0 :
                    for i in range(coun-1):
                        items =items+","+request.POST['itm'+str(i+1)]
                        quantitys =quantitys+","+request.POST['itemquantity'+str(i+1)]
                        price =price+","+request.POST['priceitem'+str(i+1)]
                        discount =discount+","+request.POST['itemdiscount'+str(i+1)]
                        amount =amount+","+request.POST['itemamount'+str(i+1)]

                Estimate_obj = Estimate(customer_id=customer_id, esti_date=esti_date, due_date=due_date, esti_no=esti_no
                , ref_no=ref_no, items=items, quantitys=quantitys, price=price, discount=discount, amount=amount, notes=notes, subtotal=subtotal, tax=tax, totalamount=totalamount)
                Estimate_obj.save()
                Estimate_Form = AddEstimateForm()
                messages.success(request, 'Estimate Added Successfully!')
                return HttpResponseRedirect('/Estimate_viewEstimate')
        else:
            Estimate_Form = AddEstimateForm()
        context = {
            'page_title':" Dashboard /",
            "product":Product.objects.all(),
            "productcount":Product.objects.all().count(),
            "estimatedata":Estimate.objects.all(),
            #'fname':fname,
            "page_path":" Dashboard",
            "menu_icon":"nav-icon fas fa-handshake",
            #"visitor_form":visitor_form,
            #"visitorData":visitorData,
           'form':Estimate_Form,
            }    
        return render(request , 'estimate/add_estimate.html', context)
    else:
        return HttpResponseRedirect("/login")   



# This views for Estimate List / Estimate Home page.
def Estimate_viewEstimate(request):
    if request.session.has_key('user'):
        return render(request , 'estimate/estimate_home.html' , {'estimate':Estimate.objects.all()})
    else:
        return HttpResponseRedirect("/login")

# This views for Delete Estimate Product.
def Estimate_deleteEstimate(request ,id):
    if request.session.has_key('user'):
        if request.method == 'POST':
            pi = Estimate.objects.get(pk=id)
            print("\n \n  delete Estimate ")
            pi.delete()
            messages.success(request, 'Estimate Deleted Successfully!')
            return HttpResponseRedirect('/Estimate_viewEstimate')
    else:
        return HttpResponseRedirect("/login")   



# This views for Update Estimate Data.
def Estimate_updateEstimate(request ,id):
    if request.session.has_key('user'):
        if request.method == 'POST':
            pi = Estimate.objects.get(pk=id)
            estimate_form = AddEstimateForm(request.POST, instance=pi)
            if estimate_form.is_valid():
                estimate_form.save()
                messages.success(request, 'Estimate Updated Successfully!')
                return HttpResponseRedirect('/Estimate_viewEstimate')
        else:
            pi = Estimate.objects.get(pk=id)
            c=list(pi.items.split(','))
            print(111111111111111111111111111)
            print(pi.items.split(','))
            itemname=[]
            for i in c:
                itemname.append(Product.objects.get(pk=int(i)).name)
            quantitys = list(pi.quantitys.split(','))
            price = list(pi.price.split(','))
            discount = list(pi.discount.split(','))
            amount = list(pi.amount.split(','))

            
            estimate_form = AddEstimateForm(instance=pi)
        context = {
            'form':estimate_form,
            'update':True,
            'itemcount':len(c),
            'itemname':itemname,
            'quantitys':quantitys,
            'price':price,
            'discount':discount,
            'amount':amount,
            'estimate':pi,
            'product':Product.objects.all(),
            'c':c,

        }
        return render(request , 'estimate/add_estimate.html', context)
    else:
        return HttpResponseRedirect("/login")     