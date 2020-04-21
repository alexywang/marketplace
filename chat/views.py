from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
import json


@login_required
def index(request):
    return render(request, 'chat/chat_index.html', {})

@login_required
def room(request, room_name=None):
    context={
        'room_name': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username))                      
    }
    return render(request, 'chat/room.html', context)


    
    
