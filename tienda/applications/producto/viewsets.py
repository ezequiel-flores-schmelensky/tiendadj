from rest_framework import viewsets
from .models import Colors, Product

from .serializers import (
    ColorSerializer, 
    ProductoSerializer,
    PaginationSerializer,
    ProductoSerializerViewSet
)


class ColorViewSet(viewsets.ModelViewSet):
    serializer_class = ColorSerializer
    queryset = Colors.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializerViewSet
    queryset = Product.objects.all()
    pagination_class = PaginationSerializer