from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class LoginForm(forms.Form):
#    user = forms.CharField(max_length = 100)
#    password = forms.CharField(widget = forms.PasswordInput())

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email', 'password1','password2']