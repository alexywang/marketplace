from django.urls import path 
import items.views

urlpatterns = [path('',items.views.index,name='index'),]
               
               