from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class AbUser(AbstractUser):
    foto = models.ImageField(upload_to='media/')
class Product(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True, null=False)
    description = models.TextField(max_length=1000, blank=False, null=False)
    types = (('Товар', 'Товар'), ('Услуга', 'Услуга'))
    type = models.CharField(choices=types, max_length=6)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name

class Basket(models.Model):
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('AbUser', on_delete=models.SET_NULL, null=True)