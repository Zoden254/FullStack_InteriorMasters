from .import views
from django.urls import path


app_name = 'e_com'
urlpatterns = [
    path('', views.home, name='home'),
    path('samples/', views.SamplesList, name='samples'),
    path('services/', views.ServicesList.as_view(), name='services'),
    path('engage/', views.about, name='engage'),
    path('login/', views.login_view, name='login'),
    path('authentication/', views.authentication, name='authentication'),
    path('comment/', views.comment, name="comment"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/', views.profile_view, name="profile"),
    path('signup/', views.signup, name="signup"),
    path('create-user/', views.create_user_view, name="create-user")
]
