
from django.contrib import admin
from django.urls import path, include

from .views import collector, UserDetailsView, login_view, userdata, Post

urlpatterns = [
    path('register/', userdata, name='register'),
    path('form/', collector, name='collector'),
    path('report', UserDetailsView.as_view(), name='report'),
    path('login/', login_view, name='_login'),
    path('', Post.as_view(), name='home'),

]
