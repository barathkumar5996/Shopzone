from django.shortcuts import render,redirect
from store.models import Product

def add_to_cart(request,id):

    product=Product.objects.get(id=id)

    cart=request.session.get('cart',{})

    if str(id) in cart:
        cart[str(id)] +=1
    else:
        cart[str(id)] =1

    request.session['cart']=cart

    return redirect('cart')


def cart(request):

    cart=request.session.get('cart',{})

    products=[]

    total=0

    for id,quantity in cart.items():

        product=Product.objects.get(id=id)

        product.quantity=quantity

        product.subtotal=product.price*quantity

        total += product.subtotal

        products.append(product)

    return render(
        request,
        'cart/cart.html',
        {
            'products':products,
            'total':total
        }
    )
def remove_from_cart(request,id):

    cart=request.session.get('cart',{})

    if str(id) in cart:

        del cart[str(id)]

    request.session['cart']=cart

    return redirect('cart')

