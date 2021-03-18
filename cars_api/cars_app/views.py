from django.shortcuts import render
from rest_framework import generics
from .serializer import CarSerializer
from .models import Car

# Create your views here.

class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer