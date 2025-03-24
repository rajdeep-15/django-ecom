from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    '''evading warning'''
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=1)
    category = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.name}"




class CartItem(models.Model):
    #user -> cart -> cartitems
    #TODO : reconsider this approach

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return f"{self.product} : {self.quantity}"