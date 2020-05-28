from django.urls import re_path, path
from . import views

app_name = "venta_app"

urlpatterns = [
    path(
        'api/venta/reporte/',
        views.ReporteVentasList.as_view(),
        name='venta-reporte'
    ),
]