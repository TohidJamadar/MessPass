from django.db import models

class Noti(models.Model):
    message = models.TextField()
    date = models.DateField()