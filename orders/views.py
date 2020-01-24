from django.shortcuts import render,redirect,reverse
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                try:
                    OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
                except:
                    pass
                cart.clear()
                order_created.delay(order.id)
            return render(request,'orders/order_created.html', {'cart': cart, 'order': order})
    else:
        form = OrderCreateForm()
    context = {'cart': cart, 'form': form}
    return render(request,'orders/order/create.html',context)


def order_created(request):
    return render(request,
                        'orders/order/created.html',
                        {'order': order})