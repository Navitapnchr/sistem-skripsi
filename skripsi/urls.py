from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SkripsiViewSet

router = DefaultRouter()
router.register(r'skripsi', SkripsiViewSet)

urlpatterns = [
    path('', include(router.urls)),
]