from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class Customer(models.Model):
#     user = models.OneToOneField(
#         User, null=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100, null=True)
#     phone = models.IntegerField(null=True)
#     email = models.EmailField(null=True)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)

#     def __str__(self):
#         return str(self.name)



class Item(models.Model):

    CATEGORY = (
        ('Bundles', 'Bundles'),
        ('Finished Products', 'Finished Products'),
        ('Raw Material', 'Raw Material'),
    )
    sku = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, null= True, choices= CATEGORY)
    tags = models.CharField(max_length=100, null= True)
    stock_status = models.FloatField()
    available_stock = models.FloatField()

    def __str__(self):
        return self.name

