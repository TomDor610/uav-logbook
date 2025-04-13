from django.shortcuts import render
from rest_framework import viewsets
from .models import Uav, Sort, Malfunction
from .serializers import UavSerializer, SortSerializer, MalfunctionSerializer

class UavViewSet(viewsets.ModelViewSet):
    queryset = Uav.objects.all()
    serializer_class = UavSerializer

class SortViewSet(viewsets.ModelViewSet):
    queryset = Sort.objects.all()
    serializer_class = SortSerializer

class MalfunctionViewSet(viewsets.ModelViewSet):
    queryset = Malfunction.objects.all()
    serializer_class = MalfunctionSerializer

# Create your views here.
