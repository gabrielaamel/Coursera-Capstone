from django.shortcuts import render
from rest_framework import  generics , viewsets

from .models import Menu, Booking
from .serializer import MenuSerializer, BookingSerializer




# Create your views here.
def index(request):
    return render(request,'index.html',{})

class MenuItemView(generics.ListCreateAPIView):
    """
    API endpoint that allows menu items to be viewed or edited.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a single menu item to be retrieved, updated, or deleted.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
        """
        API endpoint that allows bookings to be viewed or edited.
        """
        queryset = Booking.objects.all()
        serializer_class = BookingSerializer

    
