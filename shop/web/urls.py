from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index),
    path('productos/', views.products),
    path('producto/<str:reference>/', views.product),
    path('ofertas/', views.offers),
    path('clientes/', views.clients),
    path('clientes/<int:code>/', views.client),
    path('clientes/historial/', views.history),
    path('carrito/<str:reference>/', views.cart_product),
    path('carrito/<str:reference>/<int:code>/', views.cart),
]
