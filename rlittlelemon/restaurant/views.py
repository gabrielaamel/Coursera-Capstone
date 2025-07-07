from django.shortcuts import render
from rest_framework import  generics , viewsets, permissions
from django.contrib.auth.models import User
from .models import Menu, Booking
from .serializer import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
from .serializer import UserSerializer
#from rest_framework.decorators import permission_classes


# Create your views here.
def index(request):
    return render(request,'index.html',{})

class MenuItemView(generics.ListCreateAPIView):
    """
    API endpoint that allows menu items to be viewed or edited.
    """
    permission_classes = [IsAuthenticated]  # Ensure that only authenticated users can access this view
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a single menu item to be retrieved, updated, or deleted.
    """
    permission_classes = [IsAuthenticated]  # Ensure that only authenticated users can access this view
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
        """
        API endpoint that allows bookings to be viewed or edited.
        """
        queryset = Booking.objects.all()
        serializer_class = BookingSerializer
        permission_classes = [IsAuthenticated]  # Ensure that only authenticated users can access this view

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions,IsAuthenticated]  # Ensure that only authenticated users can access this view    