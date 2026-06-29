from rest_framework import viewsets
from .models import Skripsi
from .serializers import SkripsiSerializer

class SkripsiViewSet(viewsets.ModelViewSet):
    queryset = Skripsi.objects.all()
    serializer_class = SkripsiSerializer