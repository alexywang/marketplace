from django.shortcuts import render,redirect,get_object_or_404,reverse,HttpResponse
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from .forms import ItemForm
from user.models import UserProfile
from .models import *
from operator import attrgetter
from django.views.generic import UpdateView
from myutils import query_utils



@login_required
def add_item(request):
	context={}
	if request.method=='POST':
		form=ItemForm(request.POST,request.FILES)
	
		if form.is_valid() :
			item=form.save(commit=False)
			item.seller = request.user.userprofile
			item.save()
			form.save_m2m()
   
   
			return redirect('my_items')
		#return HttpResponseBadRequest('Invalid Input')
	else:
		form=ItemForm()
		
	context['form']=form
	return render(request,'items/add_item.html',context)

 
@login_required	
def edit_item(request,pk=None): 
    item = get_object_or_404(Item,pk=pk)
    context={}
    
    if item.seller==request.user.userprofile:
        
        if request.method=='POST':
            form=ItemForm(data=request.POST,files=request.FILES,instance=item)
			
            if form.is_valid():
                form.save(commit=False)
                form.save()
                form.save_m2m()
                return redirect('my_items')
            #return HttpResponseBadRequest('Invalid Input')
        else:
            form=ItemForm(instance=item)
        context['form']=form
        return render(request,'items/edit_item.html',context)
    else:
        return redirect('my_items')
            
        
@login_required	
def delete_item(request,pk=None): 
    item = get_object_or_404(Item,pk=pk)
    context={}
    
    if item.seller==request.user.userprofile:
        
        if request.method=='POST' and 'confirm' in request.POST:
            item.quantity = -1 # -1 to mark deleted item so previously made orders are preserved
            item.save()
            return redirect('my_items')
        else:
            context['item']=item
            return render(request,'items/delete_item.html',context)
    else:
        return redirect('my_items')
            


@login_required
def my_items(request):
	context={}

	myprofile= request.user.userprofile
	items = Item.objects.filter(seller=myprofile, quantity__gte=0)
	context['items']=items
	return render(request,'items/my_items.html',context)


# TODO: Update to a better search algorithm and should limit result size 
def search_item(request):
    context = {}
    items=None
    query = str(request.GET.get('q','')).lower()
    context['query'] = query

    # Get a list of users
    if str(query).strip() != '':
        # Get items that match the search by name and category
        items = Item.objects.filter(name__icontains=query) | Item.objects.filter(category__name__icontains=query)
        context['items']=items

        # Get users that match the query
        users = UserProfile.objects.filter(user__username__icontains=query)
        context['users'] = users



    return render(request, 'items/search_results.html', context)


# # Get the solo page for an item
# def item_solo_page(request):
#     context = {}
#     item_id = request.GET['item_id']
#     item = Item.objects.get(item_id=item_id)
#     context['item'] = query_utils.query_to_json([item])
#
#     return render(request, 'items/solo_listing.html', context)


# Return an item's image
# def get_item_image(request):
#     # item_id = request.GET['item_id']
#     item = Item.objects.get(item_id=7) # temp to test
#     image = item.image
#     print(type(image))
#     return HttpResponse(item.image.url, content_type='text/html')















