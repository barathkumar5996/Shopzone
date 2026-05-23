from django.contrib import admin
from .models import Product,ProductImage

class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]

admin.site.register(Product,ProductAdmin)