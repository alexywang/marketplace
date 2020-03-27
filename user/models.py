from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.TextField(max_length=30, blank=True)
    address = models.CharField(max_length=400, blank=True)

