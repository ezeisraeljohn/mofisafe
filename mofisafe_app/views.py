from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from .forms import CustomUserCreationForm
from django.contrib.auth import login


def index(request):
    return render(request, "mofisafe_app/index.html", {})

def sign_up_view(request):
    """Sign up"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts/login/')
        else:
            print(form.errors)

    form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', context={'form': form})

@login_required(login_url='accounts/login/')
def dashboard(request):
    """ The Dashboard"""
    return render(request, 'mofisafe_app/dashboard.html', {})

def about(request):
    """ About Page """
    return render(request, 'mofisafe_app/about.html', {})

def faq(request):
    """ The About page for the faq """
    return render(request, 'mofisafe_app/FAQ.html', {})

def privacy(request):
    """ Privacy """
    return render(request, 'mofisafe_app/Privacy.html', {})

def contact(request):
    """ Contact Us"""
    return render(request, 'mofisafe_app/contact.html', {})

def transaction(request):
    """ The transaction page"""
    return render(request, 'mofisafe_app/transactions.html', {})

def report(request):
    """ The report page"""
    return render(request, 'mofisafe_app/report.html', {})