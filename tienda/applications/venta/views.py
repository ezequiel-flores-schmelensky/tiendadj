from django.utils import timezone
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)
from applications.producto.models import Product
from .models import Sale, SaleDetail
from .serializers import VentaReporteSerializers, ProcesoVentaSerializer


class ReporteVentasList(ListAPIView):

    serializer_class = VentaReporteSerializers

    def get_queryset(self):

        return Sale.objects.all()


class RegistrarVenta(CreateAPIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    serializer_class = ProcesoVentaSerializer

    def create(self, request, *args, **kwargs):
        serializer = ProcesoVentaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        venta = Sale.objects.create (
            date_sale = timezone.now(),
            amount = 0,
            count = 0,
            type_invoce = serializer.validated_data['type_invoce'],
            type_payment = serializer.validated_data['type_payment'],
            adreese_send = serializer.validated_data['adreese_send'],
            user = self.request.user,
        )

        amount = 0
        count = 0

        productos = serializer.validated_data['productos']

        for producto in productos:
            prod = Product.objects.get(id=producto['pk'])
            venta_detalle = SaleDetail(
                sale=venta,
                product=prod,
                count=producto['count'],
                price_purchase=prod.price_purchase,
                price_sale=prod.price_sale,
            )
            amount = amount + prod.price_sale*producto['count']
            count = count + producto['count']
            ventas_detalle.append(venta_detalle)

        venta.amount = amount
        venta.count = count
        venta.save()
        SaleDetail.objects.bulk_create(ventas_detalle)
        return Response({'msj':'venta exitosa'})