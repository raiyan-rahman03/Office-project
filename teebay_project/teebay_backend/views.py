from django.shortcuts import render ,HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from .models import *
from .serializers import*
import logging

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class BuyProductAPIView(generics.CreateAPIView):
    serializer_class = Buy_TransactionSerializer

    def perform_create(self, serializer):

        serializer.save(user=self.request.user)
               
        return Response({"detail": " item buyed successfully."})

class RentProductAPIView(generics.CreateAPIView):
    serializer_class = Rent_TransactionSerializer

    def perform_create(self, serializer):




        # Ensure start_date and end_date are present in request data

        # Validate data using serializer
        serializer.is_valid(raise_exception=True)  # Raises ValidationError if data is invalid

        # Save the transaction with user and transaction type
        serializer.save(User=self.request.user)

        return Response({"detail": "Item rented successfully."}, status=status.HTTP_201_CREATED)
