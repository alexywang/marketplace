from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from items.models import Item
from buying.models import Cart

from user.models import UserProfile

# Create your views here
def add_to_cart(request):
    context = {}

    # force login
    if not request.user.is_authenticated:
        return HttpResponseBadRequest('login')


    # Using item ID, find the item model then add it to the user's cart
    item_id = request.GET['item_id']
    item = Item.objects.get(item_id=item_id)


    # If item is already sold return bad http request
    if item.sold:
        return HttpResponseBadRequest("sold")
    elif item.seller == request.user.userprofile:
        return HttpResponseBadRequest("ownitem")

    # Item exists, update cart and return success response
    user = request.user.userprofile
    cart = Cart.objects.get(user=user)

    # Check duplicate
    if item in cart.items.all():
        return HttpResponseBadRequest('duplicate')

    cart.items.add(item)
    return HttpResponse()

def remove_from_cart(request):
    context = {}

    #force login
    if not request.user.is_authenticated:
        return HttpResponseBadRequest('login')

    item_id = request.GET['item_id']
    item = Item.objects.get(item_id=item_id)

    user = request.user.userprofile
    cart = Cart.objects.get(user=user)
    cart.items.remove(item)

    return HttpResponse()

def get_cart(request):
    context = {}

    if not request.user.is_authenticated:
        return render(request, 'user/login.html')

    user = request.user.userprofile
    cart = Cart.objects.get(user=user)
    context['items'] = cart.items.all()

    return render(request, 'buying/cart.html', context)

