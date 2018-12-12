from django.http import HttpResponse
from django.shortcuts import render

from .models import Product
from .models import Client
from .models import Cart

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        'shop_name': "Local ecommerce",
        'products': products,
    }
    return render(request, 'web/index.html', context)

def offers(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, "web/offers.html", context)

def products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, "web/products.html", context)

def product(request, reference):
    products = Product.objects.all()
    context = {
        'products': products,
        'reference': reference,
    }
    return render(request, "web/product.html", context)

def clients(request):
    clients = Client.objects.all()
    context = {
        'clients': clients,
    }
    return render(request, "web/clients.html", context)

def client(request, code):
    client = Client.objects.get(id=code)
    context = {
        'client': client,
    }
    return render(request, "web/client.html", context)

def history(request):
    client = Client.objects.all()
    carts = Cart.objects.all()
    context = {
        'client': client,
        'carts': carts,
    }
    return render(request, "web/history.html", context)

def cart_product(request, reference):
    clients = Client.objects.all()
    products = Product.objects.all()
    context = {
        'clients': clients,
        'products': products,
        'reference': reference,
    }
    return render(request, "web/cart_product.html", context)

def cart(request, reference, code):
    #product = Product.objects.get(reference=reference)
    #cart = Cart(client=code, product=product.title)
    #cart.save()

    clients = Client.objects.all()
    products = Product.objects.all()
    context = {
        'clients': clients,
        'products': products,
        'code': code,
        'reference': reference,
    }
    return render(request, "web/cart.html", context)
