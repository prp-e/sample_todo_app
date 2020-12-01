from datetime  import date
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class TaskModel(models.Model): 
    name = models.CharField(max_length=128, blank=False) 
    summary = models.TextField() 
    start_date = models.DateField(default=date.today) 
    deadline = models.DateField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name