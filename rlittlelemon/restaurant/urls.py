from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token  # You have this
from . import views # And this
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('users/', views.UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),

    # REMOVE the 'views.' prefix here:
    path('api-token-auth/', obtain_auth_token),
] + router.urls













