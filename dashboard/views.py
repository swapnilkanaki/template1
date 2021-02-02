from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .import views
from customer.models import Customer
from invoice.models import Invoice
from estimate.models import Estimate
from pro_invoice.forms import LoginForm
from django.contrib.sessions.models import Session
from django.contrib.auth.models import auth


# Create your views here.

def login(request):
    if request.method=='GET':
        form=LoginForm()
    else:
        form=LoginForm(request.POST)    
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            if username == "admin@gmail.com" and password == "admin@123":
                request.session['user']=username
                context = {
                    'page_title':" Dashboard /",
                    "customer_count":Customer.objects.all().count(),
                    "estimate_count":Estimate.objects.all().count(),
                    "invoice_count":Invoice.objects.all().count(),
                }
                return render(request, "dashboard/index.html",context)  
            else:
                context = {'form': form} 
                return render(request, "login.html",context)  

    context = {
        'form': form
                }        
    return render(request, "login.html",context)

# Visitor Add View
def Dashboard_viewDashboard(request):
    if request.session.has_key('user'):
        context = {
            'page_title':" Dashboard /",
            "customer_count":Customer.objects.all().count(),
            "estimate_count":Estimate.objects.all().count(),
            "invoice_count":Invoice.objects.all().count(),
            #'fname':fname,
            "page_path":" Dashboard",
            "menu_icon":"nav-icon fas fa-handshake",
            #"visitor_form":visitor_form,
            #"visitorData":visitorData,
            #"branchData":branchData,
            }    
        return render(request, 'dashboard/index.html',context) 
    else:
        return redirect('/login') 


def logout(request):
    if request.session.has_key('user'):
            del request.session['user']
            auth.logout(request)
            return redirect('login')
    else:
        return redirect('/login') 