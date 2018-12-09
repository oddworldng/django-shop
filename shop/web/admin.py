from django.contrib import admin

# Register your models here.
from . models import Product
from . models import Client
from . models import Cart


admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Cart)
