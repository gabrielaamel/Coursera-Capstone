from django.db import models

# Create your models here.

class Menu(models.Model):
    Title = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=6, decimal_places=2)
    Inventory = models.IntegerField()

class Meta:
    verbose_name = 'Menu'
    verbose_name_plural = 'Menu Items'

    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'
    
class Booking(models.Model):
    Name = models.CharField(max_length=100)
    NO_of_guests = models.IntegerField()
    BookingDate = models.DateField()
    BookingTime = models.TimeField()

    def __str__(self):
        return f'{self.Name}for{self.NO_of_guests} guest om {self.BookingDate} at {self.BookingTime}'