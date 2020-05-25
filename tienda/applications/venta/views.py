from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView
)
from .models import Sale
from .serializers import VentaReporteSerializers


class ReporteVentasList(ListAPIView):

    serializer_class = VentaReporteSerializers

    def get_queryset(self):

        return Sale.objects.all()