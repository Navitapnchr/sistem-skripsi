from rest_framework import serializers
from .models import Skripsi

class SkripsiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skripsi
        fields = '__all__'