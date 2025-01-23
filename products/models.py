from django.db import models
from config.models_utils.models import TimeStampModel
from products.choices import Currency
from django.core.validators import MaxLengthValidator

class Product(TimeStampModel):
    name=models.CharField(max_length=255)
    description=models.TextField()
    price=models.FloatField()
    currency=models.CharField(max_length=255, choices=Currency.choices, default=Currency.GEL)
    quantity=models.PositiveBigIntegerField()

class Review(TimeStampModel):
    user=models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, related_name='reviews')
    product=models.ForeignKey('products.Product',on_delete=models.CASCADE,related_name='reviews')
    content=models.TextField()
    rating=models.PositiveIntegerField(validators=[MaxLengthValidator(5)])

class ProductTag(TimeStampModel):
    name=models.CharField(max_length=255)
    products=models.ManyToManyField('products.Product', related_name='product_tags')




