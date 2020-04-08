from django import forms
from .models import Item,Category
from django.forms import ModelForm



class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields=["name","description","price","quantity","image","category"]

        
        