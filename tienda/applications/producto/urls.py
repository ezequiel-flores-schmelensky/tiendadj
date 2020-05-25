from django.urls import include, re_path, path
from . import views

app_name = "product_app"

urlpatterns = [
    path(
        'api/product/por-usuario/',
        views.ListProductUser.as_view(),
        name='product-producto_by_user'
    ),
    path(
        'api/product/con-stok/',
        views.ListProductStok.as_view(),
        name='product-producto_con_stok'
    ),
    path(
        'api/product/por-genero/<gender>/',
        views.ListProductGenero.as_view(),
        name='product-producto_por_genero'
    ),
    path(
        'api/product/filtrar/',
        views.FiltrarProductos.as_view(),
        name='product-filtrar'
    ),
]