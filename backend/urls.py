from menu import views as menuViews
from django.contrib import admin
from django.urls import path
from noti import views as notiViews
from stuapi import views as stuViews
from analysis import views as anaViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/update/', menuViews.update),
    path('menu/get/', menuViews.get),
    path('noti/update/', notiViews.update),
    path('noti/get/', notiViews.get),
    path('noti/delete/', notiViews.delete),
    path('noti/post/', notiViews.post),
    path('stu/post/', stuViews.post),
    path('stu/get/', stuViews.get),
    path('stu/delete/', stuViews.delete),
    path('stu/update/', stuViews.update),
    path('stu/verify/', stuViews.verify),
    path('analysis/get_data/', anaViews.get)
]
