from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Product, Transaction
from .serializers import*

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class TransactionListAPIView(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(user=user)

class BuyProductAPIView(generics.CreateAPIView):
    serializer_class = Buy_TransactionSerializer

    def perform_create(self, serializer):

        serializer.save(user=self.request.user,
                        transaction_type = 'BUY'
                        )
        return Response({"detail": " item buyed successfully."})

class RentProductAPIView(generics.CreateAPIView):
    serializer_class = Rent_TransactionSerializer

    def perform_create(self, serializer):
        data = self.request.data

        # Ensure start_date and end_date are present in request data
        if 'rental_start_date' not in data or 'rental_end_date' not in data:
            return Response({"detail": "Start date and end date are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Validate data using serializer
        serializer.is_valid(raise_exception=True)  # Raises ValidationError if data is invalid

        # Save the transaction with user and transaction type
        serializer.save(user=self.request.user, transaction_type='RENT')

        return Response({"detail": "Item rented successfully."}, status=status.HTTP_201_CREATED)
