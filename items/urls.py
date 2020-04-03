from django.urls import path 
import items.views

urlpatterns = [path('add',items.views.add_item, name="add_item"),]
               
               