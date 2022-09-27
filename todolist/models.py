from datetime import date
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    date = models.DateField(default=date.today)
    description = models.TextField(blank=True, null=True)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title