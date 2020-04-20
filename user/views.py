from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from user.forms import UserProfileForm, UserForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from items.models import Item

import json
import sys

def index(request):
    context = {}
    context['page_type'] = 'index'
    if request.user.is_authenticated:
        username=request.user.username
    else:
        username='not logged in'

    context['username']=username
    context['items'] = Item.objects.all()
    # context['listings']=serializers.serialize('json', Item.objects.all())
    # context_json = json.dumps(context)

    return render(request,'user/index.html', context)
    # return render(request, 'user/index.html', {'context': context_json})


def register(request):
    if request.method == "POST":
        
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.is_active = False
            user.save()
            
            profile = profile_form.save(commit = False)
            profile.user = user
            profile.save()

            # Sending confirmation email
            current_site = get_current_site(request)
            mail_subject = 'Account Activation'
            message = render_to_string('user/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.id)),
                'token': account_activation_token.make_token(user)
            })
            to_email = user_form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()

            
            # username= user_form.cleaned_data.get('username')
            # password=user_form.cleaned_data.get('password1')

            # user=authenticate(username=username,password=password)
            # login(request,user)

            return render(request,'user/must_activate.html')
    else:
        user_form =UserForm()
        profile_form=UserProfileForm()
        
    context={'user_form': user_form,'profile_form': profile_form}
    return render(request,'user/register.html',context)

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request,'user/email_landing.html')
    else:
        return HttpResponse('Activation link is invalid.')


def do_login(request):
    context = {}
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)

        if form.is_valid(): 
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next')) 
                else:   
                    return redirect('index')
            else:
                form.add_error(None,'Unable to login')
    else:
        form=AuthenticationForm()
    
    context['form']=form
    return render(request,'user/login.html',context)

def do_logout(request):
    if request.user.is_authenticated:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(request.user.username, {
            'type': 'logout_message',
            'message': 'Disconnecting. You logged out from another browser or tab.'})
    logout(request)
    return redirect('login')




            

    
 
