from django.contrib import admin
from .models import Product, CartItem, Order, OrderItem

admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
