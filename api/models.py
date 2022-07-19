
from django.db import models

# Create your models here.

class User(models.model):
    url = models.URLField()
    username = models.CharField(max_length=50)
    email = models.EmailField()


class Group(models.Model):
    url = models.URLField()
    name = models.CharField(max_length=60)

