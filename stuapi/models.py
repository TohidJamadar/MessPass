from django.db import models

# Create your models here.
class User(models.Model):
    Name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=50)
    meal_left=models.IntegerField(default=60)
    daily_scan_count=models.IntegerField(default=2)
    payment_status=models.BooleanField(default=False)
    