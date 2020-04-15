from django.contrib import admin
from items.models import *
from buying.models import*
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Cart)

# Register your models here.
