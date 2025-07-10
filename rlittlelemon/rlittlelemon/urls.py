"""
URL configuration for rlittlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from rest_framework.routers import DefaultRouter
#from restaurant import views  # Import views from the restaurant app

from rest_framework.authtoken.views import obtain_auth_token
# Register the BookingViewSet with the router

#router= DefaultRouter()
#router.register(r'tables', views.BookingViewSet )

# The router will automatically create the necessary routes for the BookingViewSet
urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/', include('restaurant.urls')),
    path('', include('restaurant.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # URL for obtaining auth token
    
    path('auth/', include('djoser.urls')),  # Include Djoser's authentication URLs
    path('auth/', include('djoser.urls.authtoken')),  # Include Djoser's token authentication URLs
    

]
