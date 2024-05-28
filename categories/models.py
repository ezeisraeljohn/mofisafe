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
    user = models.ForeignKey(User, related_name='categories', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
