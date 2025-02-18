from rest_framework import viewsets
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import *
from categories.serializers import *
from categories.models import *

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = [IsAuthenticated]

class CategoryImageViewSet(viewsets.GenericViewSet, ListModelMixin, CreateModelMixin):
    serializer_class = CategoryImageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        if category_id:
            return CategoryImage.objects.filter(category_id=category_id)
        return CategoryImage.objects.none()
