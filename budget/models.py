from django.db import models
from core.models import BaseModel
from django.utils import timezone
from django.contrib.auth.models import User


class Budget(BaseModel):
    """ This class represents the budget model.

    Methods:
        __str__(): Return a human readable representation of the model instance.

    Example:
        budget = Budget(amount=1000, category='Rent', user_id=1)
        budget.save()
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    period = models.CharField(max_length=100, default='monthly')
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=None)


    def __str__(self):
        """ Return a human readable representation of the model instance. """
        return str({f'{type(self).__name__}.{self.id}: {self.__dict__}'})