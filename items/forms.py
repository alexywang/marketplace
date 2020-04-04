from django import forms
from .models import Item,Category,ItemCategories
from django.forms import ModelForm


#add categories later 
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields=["name","description","price","quantity","image"]
        
        