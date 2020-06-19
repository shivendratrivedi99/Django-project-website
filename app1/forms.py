from django.forms import ModelForm, TextInput
from django import forms
from .models import Signup
class SignupForm(forms.ModelForm):
    
    class Meta:
        model=Signup
        fields='__all__'
        widgets = {
            'fname': TextInput(attrs={'placeholder': 'First Name','class':'minwidth'}),
            'lname': TextInput(attrs={'placeholder': 'Last Name','class':'minwidth'}),
            'email': TextInput(attrs={'placeholder': 'Your Current e-mail'}),
            'phone': TextInput(attrs={'placeholder': 'Your Contact Cumber'}),
            'password': TextInput(attrs={'placeholder': 'Secret Password'}),
            'password': forms.PasswordInput(),
        }

from .models import Login
class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields='__all__'
        widgets = {
            'email': TextInput(attrs={'placeholder': 'Your Current e-mail'}),
            'password': TextInput(attrs={'placeholder': 'Secret Password'}),
            'password': forms.PasswordInput(),
        }