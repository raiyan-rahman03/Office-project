from django.urls import path
from .views import *

urlpatterns = [
    # URLs for listing and creating products
    path('products/', ProductListCreateAPIView.as_view(),
         name='product-list-create'),

    # URLs for retrieving, updating, and deleting products
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(),
         name='product-retrieve-update-destroy'),

    # URL for listing transactions of the authenticated user


    # URL for buying a product
    path('buy/', BuyProductAPIView.as_view(), name='buy-product'),

    # URL for renting a product
    path('rent/', RentProductAPIView.as_view(), name='rent-product'),
]
