from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.poll, name='poll'),
    path('pollajax', views.pollAjax, name='poll Ajax'),
]
