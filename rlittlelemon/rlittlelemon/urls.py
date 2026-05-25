
from django.contrib import admin
from django.urls import path, include
#from rest_framework.routers import DefaultRouter
#from restaurant import views  # Import views from the restaurant app

from rest_framework.authtoken.views import obtain_auth_token
# Register the BookingViewSet with the router
from django.shortcuts import redirect

#router= DefaultRouter()
#router.register(r'tables', views.BookingViewSet )

# The router will automatically create the necessary routes for the BookingViewSet
urlpatterns = [

path('admin/', admin.site.urls),
    # This brings in everything from your restaurant app's urls.py
    # keeping the API routes clean and under the 'api/' prefix.
    path('api/', include('restaurant.urls')),

# 2. Add this line to redirect the root URL to /api/
    path('', lambda request: redirect('api/')),

    # Djoser endpoints for authentication
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),


]
