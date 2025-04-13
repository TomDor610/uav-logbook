from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UavViewSet, SortViewSet, MalfunctionViewSet

router = DefaultRouter()
router.register(r'uavs', UavViewSet)
router.register(r'sorts', SortViewSet)
router.register(r'malfunctions', MalfunctionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
