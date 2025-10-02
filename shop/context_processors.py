from .models import CartItem

def cart_item_count(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        count = cart_items.count()
    else:
        cart_items = []
        count = 0
    return {'cart_items_count': count, 'cart_items': cart_items}
