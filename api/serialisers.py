from rest_framework import serializers

from .models import Aircraft, Owner

class OwnerSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Owner
        fields = ('name', 'email_address', 'phone_number')

class AircraftSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aircraft
        fields = ('registration', 'serial_number', 'aircraft_class', 'aircraft_type',
        'number_of_seats', 'cost_per_hour', 'home_base', 'owner')