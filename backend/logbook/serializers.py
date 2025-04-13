from rest_framework import serializers
from .models import Uav, Sort, Malfunction

class UavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uav
        fields = '__all__'

class SortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sort
        fields = '__all__'

class MalfunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Malfunction
        fields = '__all__'
