from django.db import models
from django.contrib .auth.models import User
# Create your models here.


class Task(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    task = models.CharField(max_length=255)
    status = models.BooleanField(default=False)