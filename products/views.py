from django.shortcuts import render 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from products.models import * 
from rest_framework import status 
from products.serializers import * 
from django.shortcuts import get_object_or_404 
from rest_framework.views import APIView 
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin,UpdateModelMixin, DestroyModelMixin


class ProductViewSet(ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,GenericAPIView): 
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def get(self,request,pk=None, *args, **kwargs): 
        if pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request  , *args ,**kwargs)
    def post(self,request, *args, **kwargs): 
        return self.create(request,*args ,**kwargs )
    def put(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def patch(self,request, *args, **kwargs):
        return self.partial_update(request,*args, **kwargs )
    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ReviewViewSet(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class=ReviewSerializer
    queryset=Review.objects.all()

    def get(self,request, *args, **kwargs):
        return self.list(request , *args ,**kwargs)
    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ProductTagView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = ProductTag.objects.all()
    serializer_class = ProductTagSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class FavoriteProductView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = FavoriteProductSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return FavoriteProduct.objects.filter(user=self.request.user)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
class CartView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return CartItem.objects.filter(cart=cart)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(cart=cart)
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)

class ProductImageViewSet(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        product_id = self.kwargs.get('product_id')
        return self.queryset.filter(product__id=product_id) if product_id else self.queryset

 



 
