from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from channels.auth import get_user, logout
from django.contrib.auth.models import User
from .models import Message,Chat
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class ChatConsumer(WebsocketConsumer):
    #creates room
    def create_room(self,room_name):
        Chat.objects.create(room_name=room_name)
    
    #Returns messages from database 
    def fetch_messages(self,data):
        chat=None
        try:
            chat=Chat.objects.get(room_name=data['room_name'])
        except Chat.DoesNotExist:
            self.create_room(data['room_name'])
            chat=Chat.objects.get(room_name=data['room_name'])
        
        #Get last 15 messages 
        messages=chat.last_15_messages()
        content={
            'command':'messages',
            'messages':self.messages_to_json(messages)
        }
        self.send_message(content)
    
    #save new message to database 
    def new_message(self,data):
        author=data['from']
        author_user=User.objects.filter(username=author)[0]
    
        message=Message.objects.create(
            author=author_user,
            content=data['message']
        )
        
        #add message to log
        current_chat=Chat.objects.get(room_name=data['room_name'])
        current_chat.messages.add(message)
        current_chat.save()
        
        content={
            'command':'new_message',
            'message':self.message_to_json(message)
        }
        return self.send_chat_message(content)
    
    def messages_to_json(self,messages):
        result=[]
        for message in messages:
            result.append(self.message_to_json(message))
        return result 
    
    def message_to_json(self,message):
        return{
            'author':message.author.username,
            'content':message.content,
            'timestamp':str(message.timestamp)
        }
    
    #functions that can be called 
    commands={
        'fetch_messages':fetch_messages,
        'new_message': new_message
        
    }
    
    #connect to room     
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
       
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )


        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self,data)
    
    def send_chat_message(self,message):
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )
    def send_message(self,message):
        self.send(text_data=json.dumps(message))

    #this isnt being used 
    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))
    
    
    # Receive message from username group
    def logout_message(self, event):
        self.close()
