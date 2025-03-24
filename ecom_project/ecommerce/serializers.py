from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product,CartItem


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ['id','username','password','email']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



class CartItemSerializer(serializers.ModelSerializer):

    product_name = serializers.ReadOnlyField(source = 'product.name')
    price = serializers.ReadOnlyField(source = 'product.price')


    class Meta:
        model = CartItem
        fields = ['id','user','product_name',"quantity",'price']
        extra_kwargs = {'user':{"read_only": True}}
