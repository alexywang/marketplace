from django.db import models
import user.models
import items.models

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    buyer  = models.ForeignKey(user.models.UserProfile, on_delete=models.SET_NULL, null=True) 
    shipping_address=models.TextField(blank=True)
    date = models.DateField()
    paid = models.BooleanField(default=False)
    
    items = models.ManyToManyField(items.models.Item)
    

