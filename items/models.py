from django.db import models
import user.models


class Category(models.Model):
    name = models.CharField(max_length=50, primary_key = True)

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,default="test item")
    seller = models.ForeignKey(user.models.UserProfile, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField(default=1)
    sold = models.BooleanField(default=False) #do we need this? or can we update once its attached to an order 
    image= models.ImageField(upload_to='item_image/',blank=True,null=True,) #python -m pip install Pillow (need this on server) 
    #also need to limit size of image


class ItemCategories(models.Model):
    item_id= models.ForeignKey(Item,on_delete=models.CASCADE)
    category_name= models.ForeignKey(Category,on_delete=models.CASCADE)


