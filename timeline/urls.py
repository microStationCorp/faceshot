from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.timelinepage, name='timeline'),
    path('vote/', views.voted, name='vote')
]
