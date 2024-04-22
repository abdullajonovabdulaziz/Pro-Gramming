from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import Users

class SignUpForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['image','first_name', 'last_name', 'email', 'username', 'password1','password2']
        widgets={
            'image': forms.FileInput(attrs={'class':'open_image'}),
            'first_name': forms.TextInput(attrs={'class': 'input', 'placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'input last_name', 'placeholder':'Last Name'}),
            'email': forms.TextInput(attrs={'class': 'input', 'placeholder':'Email', 'type':'email'}),
            'username': forms.TextInput(attrs={'class': 'input username', 'placeholder':'Username'}),
            'password1': forms.TextInput(attrs={'class': 'input password1', 'placeholder':'Password', 'type':'password'}),
            'password2': forms.TextInput(attrs={'class': 'input password2', 'placeholder':'Confirmation', 'type':'password'})
            }
        
class LogInForm(UserCreationForm):
    class Meta:
        model=Users
        fields=['username','password']
        widgets={
            'username': forms.TextInput(attrs={'class': 'input username', 'placeholder':'Username', 'name':'username'}),
            'password': forms.TextInput(attrs={'class': 'input password ', 'placeholder':'Password', 'type':'password', 'name':'password'})
            }