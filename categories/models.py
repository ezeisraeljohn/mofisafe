from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import User

class Categories(BaseModel):
    """This class represents the categories model.

    Example:
        categories = categories(name=Vacation, description='My vacation',
        date=datetime.now())
        categories.save()
    """

    category_type = {
        ('income', 'Income'),
        ('expense', 'Expense')
    }
    user = models.ForeignKey(User, related_name='categories', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(choices=category_type, default='Income', max_length=13)
    category_balance = models.DecimalField(decimal_places=2, max_digits=20, default=0.00)
    
    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"
    
    class Meta:
        unique_together = ('name', 'user', 'type')
