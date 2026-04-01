from django.urls import path
from . import views
from rest_framework import serializers


app_name = 'api'

urlpatterns = [
    path('services/', views.ServicesList.as_view()),
    path('services/<int:pk>/', views.ServiceDetail.as_view()),
    #path('users/', views.UsersList.as_view()),
]
