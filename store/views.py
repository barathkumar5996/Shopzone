from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Q


def home(request):

    products = Product.objects.all()

    return render(
        request,
        'store/home.html',
        {'products': products}
    )


def product_detail(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )

    return render(
        request,
        'store/product_detail.html',
        {'product': product}
    )


def search(request):

    q = request.GET.get('q', '')

    products = Product.objects.filter(

        Q(name__icontains=q) |
        Q(brand__icontains=q) |
        Q(category__icontains=q) |
        Q(description__icontains=q)

    )

    return render(
        request,
        'store/home.html',
        {
            'products': products,
            'query': q
        }
    )