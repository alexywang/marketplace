from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from items.models import Item
import json



@login_required
def room(request, room_name=None):
    item =get_object_or_404(Item,item_id=room_name)
    context={
        'room_name': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
        'item':item                     
    }
    return render(request, 'chat/room.html', context)


    
    
