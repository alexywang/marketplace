from django.urls import path 
import buying.views

urlpatterns = [path('add_to_cart',buying.views.add_to_cart, name="add_to_cart"),


               ]
               
               