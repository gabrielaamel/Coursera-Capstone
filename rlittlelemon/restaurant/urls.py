from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from . import views
from  rest_framework.routers import DefaultRouter
 # Register the BookingViewSet

router= DefaultRouter()
router.register(r'tables', views.BookingViewSet )


urlpatterns = [
    path('', views.index, ),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('users/', views.UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('api-token-auth/', obtain_auth_token),
    path('booking/',include(router.urls))

]
















