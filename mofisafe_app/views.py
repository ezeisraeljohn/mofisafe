from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='login/')
def home(request):
    return render(request, "mofisafe_app/home.html", {})

def sign_up_view(request):
    """Sign up"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('accounts/login/')
    
    form = UserCreationForm()
    return render(request, 'registration/signup.html', context={'form': form})