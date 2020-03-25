from django.db import models
Order(oid, email(not null), shipping addr, billing addr, total, date) (email ref Buyer) 


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    #how to refrence a seller instead of a user 
    buyer  = models.ForeignKey( 
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,required=True,null=False
    )
    shipping_address = models.TextField(max_length=500, null=False)
    billing_address = models.TextField(max_length=500, null=False)
    cart_total = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    date = models.DateField()

class put_cart(models.Model):
	order = models.ForeignKey(Order)
	item = models.ForeignKey(item)
	count=models.IntegerField(default=1)
# Create your models here.
