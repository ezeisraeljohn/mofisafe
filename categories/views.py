from django.shortcuts import render, redirect
from .forms import CategoryForm
from .models import Categories

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories_list')
    else:
        form = CategoryForm()
    return render(request, 'create_category.html', {'form': form})
