from django.db import models

# Create your models here.


class TaskList(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    area = models.CharField(max_length=50)
    leader = models.CharField(max_length=100)
