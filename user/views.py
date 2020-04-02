from django.shortcuts import render

def signup(request):
    if request.method == "POST":
        uform = UserForm(data = request.POST)
        pform = UserProfileForm(data = request.POST)
        if uform.is_valid() and pform.is_valid():
            user = uform.save()
            profile = pform.save(commit = False)
            profile.user = user
            profile.save()
#https://stackoverflow.com/questions/1727564/how-to-create-a-userprofile-form-in-django-with-first-name-last-name-modificati
#this all needs to be finished 
 
