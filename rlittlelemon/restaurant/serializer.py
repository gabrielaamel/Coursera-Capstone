from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Menu, Booking


# Serializers define the API representation.
# Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON or XML.
# Serializers also provide deserialization, allowing parsed data to be converted back into complex types,
# after first validating the incoming data.




class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id','Title','Price','Inventory'] # includes all fields in the model


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'  # '__all__' includes all fields in the model

class GroupNameField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']  # Include the groups field to show group names
        
