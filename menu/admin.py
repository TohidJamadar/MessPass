from django.contrib import admin
from .models import Menu

@admin.register(Menu)

class AdminMenu(admin.ModelAdmin):
    list_display=['day','lunch_menu','dinner_menu']
    
