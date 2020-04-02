from django.forms import ModelForm
from .models import UserProfile, User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name","email","password"]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile