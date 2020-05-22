from rest_framework.generics import (
    ListAPIView,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import render
from .models import Product
from .serializers import  ProductoSerializer


class ListProductUser(ListAPIView):
    serializer_class = ProductoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print('*************')
        usuario = self.request.user
        print(usuario)
        return Product.objects.productos_por_user(usuario)


class ListProductStok(ListAPIView):
    serializer_class = ProductoSerializer
    authentication_classes = (TokenAuthentication,) #sólo pregunta si es usuario
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        return Product.objects.productos_por_stok()

    
class ListProductGenero(ListAPIView):
    serializer_class = ProductoSerializer
    
    def get_queryset(self):
        genero = self.kwargs['gender']
        return Product.objects.productos_por_genero('m')