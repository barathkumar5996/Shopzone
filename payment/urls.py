from django.urls import path
from . import views

urlpatterns = [
    path('checkout/<int:product_id>/', views.checkout, name='checkout'),
    path('success/', views.success, name='success'),
]