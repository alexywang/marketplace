from django.urls import path 
import buying.views

urlpatterns = [path('add_to_cart',buying.views.add_to_cart, name="add_to_cart"),
               path('cart', buying.views.get_cart, name='cart'),
               path('peek_cart', buying.views.peek_cart, name='peek_cart'),
               path('orders', buying.views.get_orders, name='orders'),
               ]
               
               