from django.urls import path
from . import views

urlpatterns=[

    path(
        '',
        views.orders,
        name='orders'
    ),

    path(
        'buy/<int:id>/',
        views.buy_now,
        name='buy_now'
    )

]