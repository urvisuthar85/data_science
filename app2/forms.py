from django import forms

class Login(forms.Form):
    Firstname = forms.CharField(max_length=20)
    Password = forms.CharField(widget=forms.PasswordInput,max_length=10)