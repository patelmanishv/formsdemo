# accounts/forms.py
from django import forms

class RegistrationForm(forms.Form):
   username = forms.CharField(max_length=30)
   email = forms.EmailField()
   password = forms.CharField(widget=forms.PasswordInput)
   confirm_password = forms.CharField(widget=forms.PasswordInput)