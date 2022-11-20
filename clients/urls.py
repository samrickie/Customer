
from django.contrib import admin
from django.urls import path, include

from clients.views import collector, UserDetailsView, login_view, userdata

urlpatterns = [
    path('register/', userdata, name='register'),
    path('form/', collector, name='collector'),
    path('report<int:pk>', UserDetailsView.as_view(), name='report'),
    path('login/', login_view, name='_login'),

]
