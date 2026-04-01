from .import views
from django.urls import path


app_name = "e_com"


urlpatterns = [
    path('', views.home, name='home'),
    path('samples/', views.SamplesList.as_view(), name='samples'),
    path('services/', views.ServicesList.as_view(), name='services'),
    path('engage/', views.about, name='engage'),
    path('login/', views.login_view, name='login'),
    path('comment/', views.comment, name="comment"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/', views.profile_view, name="profile"),
    path('signup/', views.signup, name="signup"),
    path('create-user/', views.create_user_view, name="create-user"),
    path('services/<int:id>/', views.service_view, name="service_view"),
    path('add-item-to-cart/<int:id>/', views.add_item_to_cart, name="add_to_cart"),
    path('my-cart/', views.cart_view, name="cart_view"),
    path('remove-from-cart/<str:name>/', views.remove_from_cart, name="remove_from_cart"),
    path('apply-service/<int:service_id>/', views.apply_service, name="apply_service"),
    path('success/', views.success_page, name="success"),
]