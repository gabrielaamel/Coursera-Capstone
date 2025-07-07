from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from . import views
from  rest_framework.routers import DefaultRouter
 # Register the BookingViewSet

router= DefaultRouter()
router.register(r'tables', views.BookingViewSet )


urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view()),
    #path('restaurant/booking/', views.BookingViewSet.as_view({'get': 'list', 'post': 'create'})),
    #path('booking/<int:pk>/', views.BookingView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='booking-details'),
    path('api-token-auth/', obtain_auth_token),
    path('booking/',include(router.urls))

]
















