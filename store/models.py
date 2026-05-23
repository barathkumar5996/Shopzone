from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=200)

    price = models.IntegerField()

    image = models.ImageField(
        upload_to='products/'
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    brand = models.CharField(
        max_length=100,
        blank=True
    )

    category = models.CharField(
        max_length=100,
        blank=True
    )

    rating = models.FloatField(
        default=4.5
    )

    stock = models.IntegerField(
        default=1
    )

    def __str__(self):
        return self.name


class ProductImage(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )

    image = models.ImageField(
        upload_to='products/'
    )

    def __str__(self):
        return self.product.name