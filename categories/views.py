from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import NotFound

from categories.models import Category, CategoryImage
from categories.serializers import CategorySerializer, CategoryImageSerializer

class CategoryViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    
    # ufro didi dataset istvis
    pagination_class = PageNumberPagination

class CategoryImageViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    queryset = CategoryImage.objects.all()
    serializer_class = CategoryImageSerializer
    permission_classes = [IsAuthenticated]
    
    pagination_class = PageNumberPagination

    def get_queryset(self):
        category_pk = self.kwargs.get('category_pk')
        
        try:
            category = Category.objects.get(pk=category_pk)
        except Category.DoesNotExist:
            raise NotFound(detail="Category not found.")
        return self.queryset.filter(category_id=category.pk)
