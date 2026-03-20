from django.urls import path
from . import views

app_name = 'wallet'

urlpatterns = [
    path('', views.wallet, name="wallet"),
    path('deposit/', views.deposit, name="deposit"),
    path('withdraw/', views.withdraw, name="withdraw"),
    
]
