# teebay_backend/serializers.py

from rest_framework import serializers
from .models import Product, Transaction

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'rent_price', 'owner', 'categories']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
class Buy_TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields= ['id','product']
class Rent_TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields= ['id','product','rental_start_date','rental_end_date']        