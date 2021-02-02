from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'placeholder': 'Type Your Username'}),label='Username',max_length=25,min_length=3,empty_value=False,required=True)
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder': 'Type Your Password'}),label='Password',max_length=20,min_length=3,empty_value=False,required=True)
    