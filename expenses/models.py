from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from core.models import BaseModel
from categories.models import Categories


class Expense(BaseModel):
    """ This class represents the expenses model.


    Example:
        expenses = Expenses(amount=1000, category='Rent',
        date=datetime.now(), description='Rent', payment_method='Cash', user_id=1)
        expenses.save()
    """
    user = models.ForeignKey(User, related_name='expenses', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateTimeField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='expenses', limit_choices_to={'category_type': 'income'})
    description = models.TextField(null=True)
    payment_method = models.CharField(max_length=100, default=None, null=True, blank=True)

