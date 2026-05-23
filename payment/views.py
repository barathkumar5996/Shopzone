from django.shortcuts import render

def checkout(request, product_id):
    return render(request, 'payment/checkout.html')

def success(request):
    return render(request, 'payment/success.html')