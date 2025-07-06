from django.urls import path
from . import views

 # Register the BookingViewSet


urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single_menu_item'),
    path('restaurant/booking/', views.BookingViewSet.as_view({'get': 'list', 'post': 'create'})),
    #path('booking/<int:pk>/', views.BookingView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='booking-details'),
]
















