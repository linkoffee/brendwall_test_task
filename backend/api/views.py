from django.shortcuts import render
from django.conf import settings
from rest_framework import generics

from product.models import Product
from .serializers import ProductSerializer


def index(request):
    print(settings.TEMPLATES)
    return render(request, 'index/index.html')


class ProductListCreate(generics.ListCreateAPIView):
    """Вью для обработки операции с продуктами."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
