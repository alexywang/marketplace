from django.db import models
import user.models
import items.models

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    buyer  = models.ForeignKey(user.models.UserProfile, on_delete=models.SET_NULL, null=True) 
    items = models.ManyToManyField(items.models.Item)
    date = models.DateField()

