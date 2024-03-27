# teebay_backend/serializers.py

from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'rent_price', 'owner', 'categories']


class Buy_TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyTransaction
        fields= ['id','product']
class Rent_TransactionSerializer(serializers.ModelSerializer):


    class Meta:
        model = RentTransaction
        fields = ['id', 'product','rent_time']    