from django.contrib import admin
from mofisafe_app.models import Expense, Income, Budget
# Register your models here.

models = [Expense, Income, Budget]
admin.site.register(models)