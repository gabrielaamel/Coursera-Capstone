from django.test import TestCase
from .models import Menu, Booking



# Create your tests here.
class MenuTest(TestCase):

    def test_get_item(self):
        item = Menu.objects.create(Title='Pasta', Price=12.99, Inventory=10)
        self.assertEqual(item.Title, 'Pasta')
        self.assertEqual(item.Price, 12.99)
        self.assertEqual(item.Inventory, 10)

        def test_default_inventory(self):
            item = Menu.objects.create(Title='Pizza', Price=10.00)
            self.assertEqual(item.Inventory, 10) 
class BookingTest(TestCase):

    def test_booking_creation(self):
        booking = Booking.objects.create(Name='John Doe', NO_of_guests=4, BookingDate='2023-10-01', BookingTime='19:00:00')
        self.assertEqual(booking.Name, 'John Doe')
        self.assertEqual(booking.NO_of_guests, 4)
        self.assertEqual(str(booking.BookingDate), '2023-10-01')
        self.assertEqual(str(booking.BookingTime), '19:00:00')

    def test_booking_str(self):
        booking = Booking.objects.create(Name='Jane Doe', NO_of_guests=2, BookingDate='2023-10-02', BookingTime='20:00:00')
        self.assertEqual(str(booking), 'Jane Doe for 2 guest on 2023-10-02 at 20:00:00')