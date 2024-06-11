from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from core.models import BaseModel
from categories.models import Categories
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Income(BaseModel):
    """This class represents the income model
    Example:
        income = Income(amount=1000, description='Salary',
        date=datetime.now(), source='Salary', category='Salary', user_id=1)
        income.save()
    """
    user = models.ForeignKey(User, related_name='income', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    source = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, related_name='categories', limit_choices_to={'category_type': 'income'})


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
