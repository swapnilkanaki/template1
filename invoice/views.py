from django.shortcuts import render , HttpResponseRedirect
from .forms import AddInvoiceForm
from .models import Invoice
from django.contrib.auth.models import auth
from django.contrib import messages
from product.models import Product


# Create your views here.

# This views for Add New Invoice.
def Invoice_addInvoice(request):
    if request.session.has_key('user'):
        if request.method == 'POST':
            Invoice_Form = AddInvoiceForm(request.POST)
            if Invoice_Form.is_valid():
                customer_id = Invoice_Form.cleaned_data['customer_id']
                inv_date = Invoice_Form.cleaned_data['inv_date']
                due_date = Invoice_Form.cleaned_data['due_date']
                inv_no = Invoice_Form.cleaned_data['inv_no']
                ref_no = Invoice_Form.cleaned_data['ref_no']
                notes = Invoice_Form.cleaned_data['notes']
                subtotal = Invoice_Form.cleaned_data['subtotal']
                tax = Invoice_Form.cleaned_data['tax']
                totalamount = Invoice_Form.cleaned_data['totalamount']

                if request.POST['update'] =="True":
                    Invoice_obj = Invoice(customer_id=customer_id, inv_date=inv_date, due_date=due_date, inv_no=inv_no
                    , ref_no=ref_no, notes=notes, subtotal=subtotal, tax=tax, totalamount=totalamount)
                    Invoice_obj.save()
                    Invoice_Form = AddInvoiceForm()
                    messages.success(request, 'Invoice Added Successfully!')
                    return HttpResponseRedirect('/Invoice_viewInvoice')

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

                Invoice_obj = Invoice(customer_id=customer_id, inv_date=inv_date, due_date=due_date, inv_no=inv_no
                , ref_no=ref_no, items=items, quantitys=quantitys, price=price, discount=discount, amount=amount, notes=notes, subtotal=subtotal, tax=tax, totalamount=totalamount)
                Invoice_obj.save()
                Invoice_Form = AddInvoiceForm()
                messages.success(request, 'Invoice Added Successfully!')
                return HttpResponseRedirect('/Invoice_viewInvoice')
        else:
            Invoice_Form = AddInvoiceForm()
        context = {
            'page_title':" Dashboard /",
            "product":Product.objects.all(),
            "productcount":Product.objects.all().count(),
            "invoicedata":Invoice.objects.all(),
            #'fname':fname,
            "page_path":" Dashboard",
            "menu_icon":"nav-icon fas fa-handshake",
            #"visitor_form":visitor_form,
            #"visitorData":visitorData,
           'form':Invoice_Form,
            }    
        return render(request , 'invoice/add_invoice.html', context)
    else:
        return HttpResponseRedirect("/login")   



# This views for Invoice List / Invoice Home page.
def Invoice_viewInvoice(request):
    if request.session.has_key('user'):
        return render(request , 'invoice/invoice_home.html' , {'invoice':Invoice.objects.all()})
    else:
        return HttpResponseRedirect("/login")

# This views for Delete Invoice.
def Invoice_deleteInvoice(request ,id):
    if request.session.has_key('user'):
        if request.method == 'POST':
            pi = Invoice.objects.get(pk=id)
            print("\n \n  delete Invoice ")
            pi.delete()
            messages.success(request, 'Invoice Deleted Successfully!')
            return HttpResponseRedirect('/Invoice_viewInvoice')
    else:
        return HttpResponseRedirect("/login")   



# This views for Update Invoice Data.
def Invoice_updateInvoice(request ,id):
    if request.session.has_key('user'):
        if request.method == 'POST':
            pi = Invoice.objects.get(pk=id)
            Invoice_form = AddInvoiceForm(request.POST, instance=pi)
            if Invoice_form.is_valid():
                Invoice_form.save()
                messages.success(request, 'Invoice Updated Successfully!')
                return HttpResponseRedirect('/Invoice_viewInvoice')
        else:
            pi = Invoice.objects.get(pk=id)
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

            
            Invoice_form = AddInvoiceForm(instance=pi)
        context = {
            'form':Invoice_form,
            'update':True,
            'itemcount':len(c),
            'itemname':itemname,
            'quantitys':quantitys,
            'price':price,
            'discount':discount,
            'amount':amount,
            'invoice':pi,
            'product':Product.objects.all(),
            'c':c,

        }
        return render(request , 'invoice/add_invoice.html', context)
    else:
        return HttpResponseRedirect("/login")     