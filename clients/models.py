from django.contrib.auth.models import User
from django.db import models
from django.template.context_processors import media


# Create your models here.
class Userz(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = User.first_name
    last_name = User.last_name
    phone = models.CharField(max_length=20)
    email = User.email
    location = models.CharField(max_length=70)
    gender = models.CharField(max_length=10)
    username = User.username
    pasword = User.password

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Collector(models.Model):
    product_name = models.CharField(max_length=70)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()
    place = models.CharField(max_length=70)
    brand_name = models.CharField(max_length=50)
    product_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, null=True)
    Receipt_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, null=True)
    Date = models.DateTimeField(auto_now=True)
    Uzer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'products'
        verbose_name = 'product'

    def __str__(self):
        return self.product_name
