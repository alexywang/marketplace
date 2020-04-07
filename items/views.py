from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ItemForm
from .models import *



@login_required
def add_item(request):
	context={}
	if request.method=='POST':
		form=ItemForm(request.POST,request.FILES)
		if form.is_valid():
			item=form.save(commit=False)
			item.seller= request.user.userprofile
			item.save()
			return redirect('my_items')
		
	else:
		form=ItemForm()
		context['form']=form
	return render(request,'items/add_item.html',context)

@login_required
def my_items(request):
	context={}
	
	myprofile= request.user.userprofile
	items = Item.objects.filter(seller=myprofile)
	context['items']=items
	return render(request,'items/my_items.html',context)

