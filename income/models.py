from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from core.models import BaseModel

class Income(BaseModel):
    """This class represents the income model.

    Methods:
        __str__(): Return a human readable representation of the model instance.

    Example:
        income = Income(amount=1000, description='Salary',
        date=datetime.now(), source='Salary', category='Salary', user_id=1)
        income.save()
    """
    user = models.ForeignKey(User, related_name='income', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    source = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default='')

