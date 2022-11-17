
from django.contrib import admin
from django.urls import path, include

from clients.views import register, collector

urlpatterns = [
    path('register/', register, name='register'),
    path('form/', collector, name='collector'),
]
