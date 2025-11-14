from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:categories_list')

class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:products_list')
