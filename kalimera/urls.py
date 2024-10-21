from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    path('admin/', admin.site.urls),  # The admin site
    path('', include('mainapp.urls')),  # Include app-specific URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Django's built-in authentication system
]
