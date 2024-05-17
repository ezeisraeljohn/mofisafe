from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

categories_expenses = ['Food', 'Emergency', 'Clothing', 'Housing', 'Health', 'Others']
categories_income = ['Freelancing', 'Salary', 'Others']

class Income(models.Model):
    """This class represents the income model.

    Attributes:
        amount (int): The amount of the income.
        description (str): A description of the income.
        date (date): The date the income was received.
        source (str): The source of the income.
        category (str): The category of the income.
        user_id (int): The user_id of the user that owns the income.


    Methods:
        __str__(): Return a human readable representation of the model instance.

    Example:
        income = Income(amount=1000, description='Salary',
        date=datetime.now(), source='Salary', category='Salary', user_id=1)
        income.save()
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    source = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField(default='', null=True)
    category = models.CharField(max_length=100, default='')

    def __str__(self):
        """ Return a human readable representation of the model instance. """
        return str({f'{type(self).__name__}.{self.id}: {self.__dict__}'})
        
    
class Expense(models.Model):
    """ This class represents the expenses model.

    Attributes:
        amount (int): The amount of the expenses.
        category (str): The category of the expenses.
        date (date): The date the expenses was incurred.
        description (str): A description of the expenses.
        payment_method (str): The payment method used for the expenses.
        user_id (int): The user_id of the user that incurred the expenses.

    Methods:
        __str__(): Return a human readable representation of the model instance.

    Example:
        expenses = Expenses(amount=1000, category='Rent',
        date=datetime.now(), description='Rent', payment_method='Cash', user_id=1)
        expenses.save()
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    category = models.CharField(max_length=100, default='')
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField(default='', null=True)
    payment_method = models.CharField(max_length=100, default=None)

    def __str__(self):
        """ Return a human readable representation of the model instance. """
        return str({f'{type(self).__name__}.{self.id}: {self.__dict__}'})
        

class Budget(models.Model):
    """ This class represents the budget model.

    Attributes:
        amount (int): The amount of the budget.
        category (str): The category of the budget.
        user_id (int): The user_id of the user that owns the budget.

    Methods:
        __str__(): Return a human readable representation of the model instance.

    Example:
        budget = Budget(amount=1000, category='Rent', user_id=1)
        budget.save()
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)

    period = models.CharField(max_length=100, default='monthly')
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=None)


    def __str__(self):
        """ Return a human readable representation of the model instance. """
        return str({f'{type(self).__name__}.{self.id}: {self.__dict__}'})