from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from items.models import Item
from buying.models import *

from user.models import UserProfile


def add_to_cart(request):
    context = {}

  
    if not request.user.is_authenticated:
        return HttpResponseBadRequest('login')

    # Using item ID, find the item model then add it to the user's cart
    item_id = request.GET['item_id']
    quantity = request.GET['quantity']
    # quantity = 2
    print('quantity: ' + str(quantity))
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
        cart_item.quantity = quantity
        cart_item.save()
        return HttpResponse('updated')
    else: # Create new cart entry
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


def remove_from_cart(request):
    context = {}

    #force login
    if not request.user.is_authenticated:
        return HttpResponseBadRequest('login')

    item_id = request.GET['item_id']
    item = Item.objects.get(item_id=item_id)

    user = request.user.userprofile
    cart_item = get_cart_item(user, item)
    if cart_item:
        cart_item.delete()

    return HttpResponse()

def get_cart(request):
    context = {}

    if not request.user.is_authenticated:
        return render(request, 'user/login.html')
    user = request.user.userprofile
    _validate_cart(user)

    # Get cart items
    cart_items = CartItem.objects.filter(user=user)
    items = [x.item for x in cart_items]

    # Get cart total
    total_price = 0
    for item in items:
        total_price += item.price

    if request.method == 'GET': # View Cart
        context['items'] = items
        context['total_price'] = total_price
        return render(request, 'buying/cart.html', context)
    else: # Order the cart
        #TODO: Post functionality for ordering
        shipping = request.POST['shipping_address']
        print(shipping)
        # Update item listing quantity
        # for cart_item in cart_items:
        #     cart_item.item.quantity -= cart_item.quantity
        #

        # Create orders
        for cart_item in cart_items:
            # Update quantity on listing
            cart_item.item.quantity -= cart_item.quantity
            order = Order(buyer=user, shipping_address=shipping, item=cart_item.item, quantity=cart_item.quantity, price=cart_item.quantity*cart_item.item.price)
            cart_item.item.save()
            order.save()

        return HttpResponse("Checkout")

# for a user validate their cart (i.e. delete items that dont exist anymore or are sold out)
def _validate_cart(profile):
    valid = True
    cart_items = CartItem.objects.filter(user=profile)
    for cart_item in cart_items:
        if not cart_item.item or cart_item.item.quantity == 0:
            cart_item.delete()
            valid = False
    return valid








