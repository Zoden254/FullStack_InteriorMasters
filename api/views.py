from e_com.models import Service
from rest_framework import generics
from .serializers import *
from .serializers import ServicesSerializer

class ServicesList(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServicesSerializer