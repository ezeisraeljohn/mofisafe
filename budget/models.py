from django.db import models
from core.models import BaseModel
from django.utils import timezone
from django.contrib.auth.models import User


class Budget(BaseModel):
    """ This class represents the budget model.

    Example:
        budget = Budget(amount=1000, category='Rent', user_id=1)
        budget.save()
    """
    user = models.ForeignKey(User, related_name='budgets', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    period = models.CharField(max_length=100, default='monthly')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
