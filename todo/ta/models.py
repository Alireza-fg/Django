from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title=models.CharField(max_length=100)
    status=models.BooleanField(default=False)
    
    