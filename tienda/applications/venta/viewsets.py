from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from applications.producto.models import Product
from .serializers import ProcesoVentaSerializer2, VentaReporteSerializers
from .models import Sale, SaleDetail


class VentasViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    #permission_classes = [IsAuthenticated]
    #serializer_class = VentaReporteSerializers
    queryset = Sale.objects.all()

    def get_permissions(self):
        if (self.action == 'list') or (self.action == 'retrieve'):
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

    #Cuando se trabaje con view set se necesita redefinir los metodos list, retrive, etc...
    def list(self, request,*args, **kwargs):
        queryset = Sale.objects.all()
        serializer = VentaReporteSerializers(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProcesoVentaSerializer2(data=request.data)
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

    def retrieve(self, request, pk=None):
        #venta = Sale.objects.get(id=pk)
        venta = get_object_or_404(Sale.objects.all(), pk=pk) 
        serializer = VentaReporteSerializers(venta)
        #print('************')
        return Response(serializer.data)