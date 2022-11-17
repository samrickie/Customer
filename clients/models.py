from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=70)
    gender = models.CharField(max_length=10)
    username = models.CharField(max_length=20, unique=True)
    pasword = models.CharField(max_length=30)

    class Meta:
        ordering = ['first_name']
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
    product_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    Receipt_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

    class Meta:
        verbose_name_plural = 'products'
        verbose_name = 'product'

    def __str__(self):
        return self.product_name
