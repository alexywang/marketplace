from django.db import models
import user.models
import items.models

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    buyer  = models.ForeignKey(user.models.UserProfile, on_delete=models.SET_NULL, null=True) 
    shipping_address=models.TextField(blank=True)
    date = models.DateField()
    # paid = models.BooleanField(default=False)
    
    items = models.ManyToManyField(items.models.Item)

class CartItem(models.Model):
    cart_item_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(user.models.UserProfile, on_delete=models.CASCADE)
    item = models.ForeignKey(items.models.Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ('user', 'item')


# class Cart(models.Model):
#     cart_id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(user.models.UserProfile, on_delete=models.CASCADE)
#     items = models.ManyToManyField(items.models.Item)
#
#     class Meta:
#         ordering = ('cart_id',)
#         def __str__(self):
#             return self.name