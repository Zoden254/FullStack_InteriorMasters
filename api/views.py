from e_com.models import *
from rest_framework import permissions
from rest_framework import generics
from .serializers import *
from .serializers import ServicesSerializer

class ServicesList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServicesSerializer

class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServicesSerializer

class UsersList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]