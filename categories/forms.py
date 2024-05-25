from django import forms
from .models import Categories
from django.core.exceptions import ValidationError

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Categories
        fields = ("name", "description")

    def clean_name(self):
        name = self.clean_data.get('name')
        if not name:
            raise ValidationError('This fiel is required.')
        if len(name) < 3:
            raise ValidationError('Name must be at least 3 characters long')
        if len(name) > 50:
            raise ValidationError('Name must be less than 50 characters long')
        if Categories.objects.filter(name=name).exists():
            raise ValidationError('Category with this name exists.')
        return (name)

