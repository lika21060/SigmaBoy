from django.db import models
from config.model_utils.models import TimeStampModel

class Category(TimeStampModel):
    name = models.CharField(max_length=255, unique=True)
    products = models.ManyToManyField('products.Product', related_name='categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class CategoryImage(TimeStampModel):
    category = models.ForeignKey('categories.Category', related_name='images', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to='categories/')

    def __str__(self):
        return f"Image for {self.category.name}"

    class Meta:
        verbose_name = "Category Image"
        verbose_name_plural = "Category Images"
