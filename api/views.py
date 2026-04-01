from e_com.models import Service
from rest_framework import generics
from .serializers import *
from .serializers import ServicesSerializer

class ServicesList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServicesSerializer

class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServicesSerializer