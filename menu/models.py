from django.db import models

# Create your models here.
class Menu(models.Model):
    day = models.CharField(max_length=10, unique=True)
    lunch_menu = models.TextField()
    dinner_menu = models.TextField()