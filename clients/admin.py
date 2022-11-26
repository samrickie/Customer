from django.contrib import admin

from .models import Userz, Collector,Post

# Register your models here.
admin.site.register(Userz)
admin.site.register(Collector)
admin.site.register(Post)