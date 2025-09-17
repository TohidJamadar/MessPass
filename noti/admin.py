from django.contrib import admin
from .models import Noti

@admin.register(Noti)

class AdminMenu(admin.ModelAdmin):
    list_display=['message','date']
    
