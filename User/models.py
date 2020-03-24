from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.TextField(max_length=30, blank=True)
    address = models.CharField(max_length=400, blank=True)


@receiver(post_save, sender=User)
def create_user_seller(sender, instance, created, **kwargs):
    if created:
        Seller.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_seller(sender, instance, **kwargs):
    instance.seller.save()

#Buyer will just be a default user!
