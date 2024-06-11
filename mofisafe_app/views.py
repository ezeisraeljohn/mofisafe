from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth import login, logout
from django.urls import reverse
from django.contrib import messages

def index(request):
    return render(request, "mofisafe_app/index.html", {})

def sign_up_view(request):
    """Sign up"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect(reverse('login'))
        else:
            print(form.errors)

    form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', context={'form': form})

@login_required(login_url='accounts/login/')
def dashboard(request):
    """ The Dashboard"""
    return render(request, 'mofisafe_app/dashboard.html', {})

def logout_view(request):
    """logout"""
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect(reverse('login'))

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

def profile(request):
    """ The profile page"""
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    context = {
        'profile_form': profile_form
    }
    return render(request, 'mofisafe_app/profile.html', context)