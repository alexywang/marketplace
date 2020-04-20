from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from items.models import Item
from buying.models import *
import django.core.serializers
from myutils import query_utils

import json
from user.models import UserProfile


def add_to_cart(request):
    if not request.user.is_authenticated:
        return HttpResponseBadRequest('login')

    # Using item ID, find the item model then add it to the user's cart
    item_id = request.GET['item_id']
    quantity = request.GET['quantity']
    item = Item.objects.get(item_id=item_id)


    # If item is already sold return bad http request
    if item.quantity == 0:
        return HttpResponseBadRequest("sold")
    elif item.seller == request.user.userprofile:
        return HttpResponseBadRequest("ownitem")

    # Item exists, update cart and return success response
    user = request.user.userprofile

    cart_item = get_cart_item(user, item)

    # Check if item is already in the user's cart
    if cart_item:
        print('Updating quantity to ' + str(quantity))
        cart_item.quantity = quantity
        if int(quantity) == 0: # Remove from cart instead
            print('DELETING CART ITEM')
            cart_item.delete()
            return HttpResponse('removed')
        else: # Update quantity
            cart_item.save()
            return HttpResponse('updated')
    else: # Create new cart entry
        if int(quantity) == 0:
            return HttpResponseBadRequest('noquantity')
        else:
            print('NEW')
            cart_item = CartItem(item=item, user=user, quantity=quantity)
            cart_item.save()
            return HttpResponse('added')

# Check if a user already has an item in their cart
def get_cart_item(user, item):
    try:
        cart_item = CartItem.objects.get(user=user, item=item)
        return cart_item
    except CartItem.DoesNotExist:
        return None

# Simple GET endpoint to return the user's cart for front end processing
def peek_cart(request):

    if not request.user.is_authenticated:
        return HttpResponseBadRequest()

    # query the user's cart
    user = request.user.userprofile
    cart_model = CartItem.objects.filter(user=user)
    resp = dict()
    resp['cart'] = []
    for cart_item in cart_model:
        resp['cart'].append(
            {'item_id': cart_item.item.item_id,
             'quantity': cart_item.quantity
             }
        )
    return HttpResponse(json.dumps(resp), content_type="application/json")


# Show user cart and form to checkout
def get_cart(request):
    context = {}
    context['page_type'] = 'cart'

    if not request.user.is_authenticated:
        return render(request, 'user/login.html')
    user = request.user.userprofile

    # TODO: Handle a special notification if cart items have changed due to invalid carts.
    valid_cart = _validate_cart(user)
    context['valid_cart'] = valid_cart
    context['order_failure'] = False

    # Get cart items
    cart_items = CartItem.objects.filter(user=user)
    items = [x.item for x in cart_items]

    # Get cart total
    total_price = 0
    for cart_item in cart_items:
        total_price += cart_item.item.price*cart_item.quantity

    context['items'] = items
    context['total_price'] = total_price

    if request.method == 'GET': # View Cart
        return render(request, 'buying/cart.html', context)

    else: # Order the cart
        if not valid_cart: # if the cart is no longer valid then notify refresh the cart and notify user
            context['order_failure'] = True
            return render(request, 'buying/cart.html', context)
        else:
            context['order_failure'] = False

        #TODO: Post functionality for ordering
        shipping = request.POST['shipping_address']

        # Create orders
        for cart_item in cart_items:
            cart_item.item.quantity -= cart_item.quantity # Update quantity on listing

            #Create Order
            order = Order(buyer=user, shipping_address=shipping, item=cart_item.item, quantity=cart_item.quantity, price=cart_item.quantity*cart_item.item.price)
            cart_item.item.save()
            order.save()

            # Delete item from their cart
            cart_item.delete()

        return redirect('orders')

# for a user validate their cart (i.e. delete items that dont exist anymore or are sold out)
def _validate_cart(profile):
    valid = True
    cart_items = CartItem.objects.filter(user=profile)
    for cart_item in cart_items:
        if cart_item.item.quantity < cart_item.quantity or cart_item.item.quantity == 0:
            cart_item.delete()
            valid = False
    return valid


# To see a user's past orders
def get_orders(request):
    context = {}
    # Force login
    if not request.user.is_authenticated:
        return render(request, 'user/login.html')

    user = request.user.userprofile

    # Get orders made by the user
    my_purchases = Order.objects.filter(buyer=user).order_by('-date')
    my_purchases_json = query_utils.query_to_json(my_purchases, exclude_fields="password")
    context['my_purchases'] = my_purchases_json

    # Get orders made to the user
    my_orders = Order.objects.filter(item__seller=user).order_by('-date')
    print(len(my_orders))
    my_orders_json = query_utils.query_to_json(my_orders, exclude_fields="password")
    context['my_orders'] = my_orders_json


    return render(request, 'buying/orders.html', context)







