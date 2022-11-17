from django.contrib import admin

from clients.models import User, Collector

# Register your models here.
admin.site.register(User)
admin.site.register(Collector)
