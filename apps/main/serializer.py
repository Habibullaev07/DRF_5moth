from pyexpat import model
from rest_framework import serializers
from apps.main.models import Settings, ProductImage, Products, Characteristic

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = "__all__"
        
class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    
    class Meta:
        model = ProductImage
        fields = ['image', 'position']
        
class ProductSerializer(serializers.ModelSerializer):
    product_image = ProductImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Products
        fields = ['id', 'title', 'description', 'price', 'is_active', 'product_image', 'created_at']


class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = "__all__"
