from django.db import models
import user.models


class Category(models.Model):
    name = models.CharField(max_length=50, primary_key = True)

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    seller = models.ForeignKey(user.models.UserProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField(default=1)
    sold = models.BooleanField(default=False)

