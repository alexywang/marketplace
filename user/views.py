from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from user.forms import UserProfileForm, UserForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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
            
            profile = profile_form.save(commit = False)
            profile.user = user
            profile.save()
            
            username= user_form.cleaned_data.get('username')
            password=user_form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password) 
            login(request,user)
            
            return redirect('index')
    else:
        user_form =UserForm()
        profile_form=UserProfileForm()
        
    context={'user_form': user_form,'profile_form': profile_form}
    return render(request,'user/register.html',context)

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
                print('Login fail')
                form.add_error(None,'Unable to login')
        else:
            print('form invalid')
    else:
        print('Serving form')
        form=AuthenticationForm()
    context['form']=form
    return render(request,'user/login.html',context)

def do_logout(request):
    logout(request)
    return redirect('login')
    
            
            
            

    
 
