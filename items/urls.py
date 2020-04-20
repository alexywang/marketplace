from django.urls import path 
import items.views


#what naming convention do we want to use 
urlpatterns = [path('add',items.views.add_item, name="add_item"),
               path('myItems',items.views.my_items,name="my_items"),
               path('edit/<int:pk>',items.views.edit_item,name="edit_item"),
               path('search', items.views.search_item, name="search"),
               path('delete/<int:pk>',items.views.delete_item,name="delete_item"),
               # path('item_image', items.views.get_item_image, name='item_image'),
               # path('solo_listing', items.views.item_solo_page, name='solo_listing')
            ]

               