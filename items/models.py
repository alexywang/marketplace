from django.db import models
from django.conf import settings


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    #how to refrence a seller instead of a user 
    seller  = models.ForeignKey( 
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,required=True
    )
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2,required=True)
    inventory = models.IntegerField(default=0)

class Category(models.Model):
	category_id  = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)

class ItemCategories(models.Model):
	category_id  = models.ForeignKey(Category,on_delete=models.CASCADE)
	item_id=models.ForeignKey(Item,on_delete=models.CASCADE)

