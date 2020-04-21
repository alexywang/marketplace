from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Message(models.Model):
    author =models.ForeignKey(User,related_name='author_messages',on_delete=models.CASCADE)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.author.username

class Chat(models.Model):
    room_name=models.CharField(unique=True,max_length=10)
    participants=models.ManyToManyField(User,related_name='chats',blank=True)
    messages = models.ManyToManyField(Message,blank=True)
    
    def last_15_messages(self):
        return self.messages.order_by('-timestamp').all()[:15]
    
    def __str__(self):
        return "{}".format(self.pk)    
    