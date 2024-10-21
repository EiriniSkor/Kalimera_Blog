from mainapp import views
from django.urls import path

app_name = 'mainapp'  

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('register/', views.register, name='register'),  # Registration view
    path('login/', views.user_login, name='user_login'),  # Custom login view 
    path('profile/', views.profile, name='profile'),  # Profile page
]
