from django.db import models
import user.models
import items.models

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    buyer  = models.ForeignKey(user.models.UserProfile, on_delete=models.SET_NULL, null=True) # Removed cascading so previous orders will still show if the buyer gets deleted
    item = models.ForeignKey(items.models.Item, on_delete=models.SET_NULL, null=True)
    date = models.DateField()

class UserCartItem(models.Model):
    user = models.ForeignKey(user.models.UserProfile, on_delete=models.CASCADE)
    item = models.ForeignKey(items.models.Item, on_delete=models.CASCADE)
