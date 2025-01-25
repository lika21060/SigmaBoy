from django.contrib import admin
from products.models import Product, Review, ProductTag

admin.site.register(Product)
admin.site.register(Review)
admin.site.register(ProductTag)

