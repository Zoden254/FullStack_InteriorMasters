from django.urls import path
from . import views

app_name = 'message_app'
urlpatterns = [
    path('', views.messages, name="messages"),
    path('chat/', views.find_user, name="find_user"),
    path('chat/<str:user_number>/', views.chat, name="chat"),
    path('sent/<str:user_number>/', views.message_sent, name="sent"),
]
