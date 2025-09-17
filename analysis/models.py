from django.db import models

class Data(models.Model):
    day=models.CharField(max_length=10)
    count=models.IntegerField()
