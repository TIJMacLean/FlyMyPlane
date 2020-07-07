from django.shortcuts import render
from rest_framework import viewsets

from .serialisers import OwnerSerialiser, AircraftSerialiser
from .models import Owner, Aircraft

# Create your views here.

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all().order_by('name')
    serializer_class = OwnerSerialiser

class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all().order_by('registration')
    serializer_class = AircraftSerialiser