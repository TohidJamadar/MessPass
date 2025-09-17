from django.contrib import admin
from .models import User

@admin.register(User)

class AdminUser(admin.ModelAdmin):
    list_display=['id','Name','email','password', 'meal_left','daily_scan_count','payment_status']
    
