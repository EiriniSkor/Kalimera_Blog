from django import forms
from django.contrib.auth.models import User
from mainapp.models import UserProfileInfo
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model= User
        fields = ('username', 'email', 'password',)
        
    
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Email field added

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Optional Login Form (if you want custom handling)
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
