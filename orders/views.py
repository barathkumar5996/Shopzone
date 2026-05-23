from django.shortcuts import render
from store.models import Product

def buy_now(request,id):

    product = Product.objects.get(id=id)

    return render(
        request,
        'orders/checkout.html',
        {
            'product': product
        }
    )


def orders(request):
    return render(request,'orders/orders.html')