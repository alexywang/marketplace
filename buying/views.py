from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from items.models import Item
from buying.models import CartItem

from user.models import UserProfile

# Create your views here
def add_to_cart(request):
    context = {}

    # force login
    if not request.user.is_authenticated:
        return HttpResponseBadRequest('login')

    #TODO: Handle quantities

    # Using item ID, find the item model then add it to the user's cart
    item_id = request.GET['item_id']
    quantity = request.GET['quantity']
    print('quantity: ' + quantity)
    item = Item.objects.get(item_id=item_id)


    # If item is already sold return bad http request
    if item.sold or item.quantity == 0:
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
    # cart = Cart.objects.get(user=user)
    # cart.items.remove(item)

    return HttpResponse()

def get_cart(request):
    context = {}

    if not request.user.is_authenticated:
        return render(request, 'user/login.html')

    if request.GET:

        user = request.user.userprofile
        cart_items = CartItem.objects.filter(user=user)
        items = [x.item for x in cart_items]
        context['items'] = items
        return render(request, 'buying/cart.html', context)
    else:
        #TODO: Post functionality for ordering
        return HttpResponseBadRequest()

