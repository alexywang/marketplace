from django.db import models
import user.models

def user_directory_path(instance, filename):
    return 'item_image/user_{0}/{1}'.format(instance.seller.id, filename)


class Category(models.Model):
    name = models.CharField(max_length=50, primary_key = True)
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    seller = models.ForeignKey(user.models.UserProfile, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField(default=1)
    sold = models.BooleanField(default=False) #do we need this? or can we update once its attached to an order 
    image= models.ImageField(upload_to=user_directory_path,blank=True,null=True) #python -m pip install Pillow (need this on server) 
    category=models.ManyToManyField(Category)
    date_uploaded=models.DateField(auto_now=True)
    
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name





