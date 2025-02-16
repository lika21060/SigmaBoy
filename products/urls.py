from django.urls import path
from .views import ProductViewSet, ReviewViewSet, ProductTagView, FavoriteProductView, CartView

urlpatterns = [
    path('products/', ProductViewSet.as_view(), name='product-list'), 
    path('products/<int:pk>/', ProductViewSet.as_view(), name='product-detail'), 
    path('reviews/', ReviewViewSet.as_view(), name='review-list'),
    
    path('product-tags/', ProductTagView.as_view(), name='product-tag-list'),
    path('favorite-products/', FavoriteProductView.as_view(), name='favorite-product-list'), 
    path('cart/', CartView.as_view(), name='cart-list'), 
]
