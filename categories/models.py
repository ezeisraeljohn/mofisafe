from django.db import models
from core.models import BaseModel

class Categories(BaseModel):
    """This class represents the categories model.

    Example:
        categories = categories(name=Vacation, description='My vacation',
        date=datetime.now())
        categories.save()
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
