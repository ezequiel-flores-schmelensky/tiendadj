from rest_framework.generics import (
    ListAPIView,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
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
        return Product.objects.productos_por_user(usuario)