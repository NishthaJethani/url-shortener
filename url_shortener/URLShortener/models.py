from pickle import TRUE
from django.db import models

# Create your models here.
class LongtoShort(models.Model):
    long_url=models.URLField(max_length=500)
    custom_name=models.CharField(max_length=50, unique=True)
    created_date=models.DateField(auto_now_add=True)
    clicks=models.IntegerField(default=0)
