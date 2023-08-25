# accounts/views.py
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
   if request.method == 'POST':
       form = RegistrationForm(request.POST)
       if form.is_valid():
           # Process the form data (registration logic)
           return redirect('registration_success')
   else:
       form = RegistrationForm()
   return render(request, 'accounts/register.html', {'form': form})

def registration_success(request):
    return render(request, 'accounts/registration_success.html')