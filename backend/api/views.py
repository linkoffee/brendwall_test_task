from django.shortcuts import render
from rest_framework import generics

from product.models import Product
from .serializers import ProductSerializer


def index(request):
    return render(request, 'index/index.html')


class ProductListCreate(generics.ListCreateAPIView):
    """Вью для обработки операции с продуктами."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
