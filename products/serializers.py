from rest_framework import serializers
from products.models import *


#no need for fields bc theyre automarically included with

class ProductSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'currency', 'quantity', 'images']


class CartSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True, required=False)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'products']

    def validate_products(self, value):
        #make sure all product ids are included
        for product in value:
            if not Product.objects.filter(id=product.id).exists():
                raise serializers.ValidationError(f"Product with id {product.id} does not exist.")
        return value

class ReviewSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Review
        fields = ['id', 'user', 'product', 'content', 'rating']

    def validate_rating(self, value):
        #Rating must be between 1 and 5
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value

    def create(self, validated_data):
      
        user = self.context['request'].user
        return Review.objects.create(user=user, **validated_data)


class ProductTagSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)

    class Meta:
        model = ProductTag
        fields = ['id', 'name', 'products']

    def validate_name(self, value):
        #tag name cannot be empty and should have a maximum of 50 characters.
        if not value.strip():
            raise serializers.ValidationError("Tag name cannot be empty.")
        if len(value) > 50:
            raise serializers.ValidationError("Tag name is too long. Maximum 50 characters allowed.")
        return value


class FavoriteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteProduct
        fields = ['id', 'user', 'product']
        read_only_fields = ['user']  # User is automatically assigned

    def validate(self, data):
        
        user = self.context['request'].user
        product = data.get('product')

        if FavoriteProduct.objects.filter(user=user, product=product).exists():
            raise serializers.ValidationError("This product is already in your favorites.")
        return data


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'product']
