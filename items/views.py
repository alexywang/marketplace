from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def add_item(request):
	return render(request,'items/add_item.html')

