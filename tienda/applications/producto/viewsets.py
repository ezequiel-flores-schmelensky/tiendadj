from rest_framework import viewsets
from rest_framework.response import Response
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

    def perform_create(self, serializer):
        serializer.save(
            video="https://youtu.be/h8a1gLl9C5A"
        )

    def list(self, request,*args, **kwargs):
        queryset = Product.objects.productos_por_user(self.request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)