from rest_framework.routers import DefaultRouter
from . import viewsets


router = DefaultRouter()
router.register(r'colors', viewsets.ColorViewSet, basename="colors")
urlpatterns = router.urls