from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ServiceSerializer
from .models import Service

class ServiceView(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()