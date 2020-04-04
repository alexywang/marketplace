from django.shortcuts import render,redirect
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
import sys

def index(request):
    context = {}
    if request.user.is_authenticated:
        username=request.user.username
    else:
        username='not logged in'

    context['username']=username
    return render(request,'user/index.html',context)


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

            return HttpResponse('Check your email for the activation link.')
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
        return HttpResponse('Thank you for registering, you can now login to your account')
    else:
        return HttpResponse('Activation link is invalid.')


def do_login(request):
    context = {}
    if request.method=='POST':
        print('Got POST')
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                form.add_error(None,'Unable to login')
    else:
        form=AuthenticationForm()
    context['form']=form
    return render(request,'user/login.html',context)

def do_logout(request):
    logout(request)
    return redirect('login')
    

            

            



#https://stackoverflow.com/questions/1727564/how-to-create-a-userprofile-form-in-django-with-first-name-last-name-modificati
#this all needs to be finished 
 
