from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, CartItem, Order, OrderItem
from django.contrib.auth.decorators import login_required

# Home page view
def home(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products})

# Add to cart view
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('home')

# Cart page view
@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'shop/cart.html', {'cart_items': cart_items})

# Checkout view
@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if request.method == 'POST':
        order = Order.objects.create(user=request.user)
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
        cart_items.delete()  # Clear cart after checkout
        return redirect('home')
    return render(request, 'shop/checkout.html', {'cart_items': cart_items})
