from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.sessions.models import Session
# Create your views here.

"""def login(request):
    if request.method=='GET':
        form=LoginForm()
    else:
        form=LoginForm(request.POST)    
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            if username == "admin" and password == "admin":
                request.session['user']=username
                print(request.session['user'])
                # return redirect('dashboard')
                return render(request, "dashboard/index_layout.html")  
            else:
                context = {'form': form} 
                return render(request, "login.html",context)  

    context = {
        'form': form
                }        
    return render(request, "login.html",context) """
