from django.urls import path, include
from rest_framework_nested import routers
from products.views import *

router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('tags', ProductTagViewSet, basename='tags')

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('images', ProductImageViewSet, basename='product-images')
products_router.register('reviews', ReviewViewSet, basename='product-reviews')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(products_router.urls)),

    path('favorite_products/', FavoriteProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='favorite_products'),
    path('favorite_products/<int:pk>/', FavoriteProductViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name='favorite_product'),

    path('cart/', CartViewSet.as_view({'get': 'list', 'post': 'create'}), name='cart'),
]
