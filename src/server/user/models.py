from django.db import models

# Create your models here.
class User(models.Model):
    """
    User table
    """
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
