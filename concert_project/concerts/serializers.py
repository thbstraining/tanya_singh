from rest_framework import serializers
from .models import Concert, SeatingLayout, Reservation

class ConcertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concert
        fields = '__all__'

    def validate_name(self, value):
        # Check if a concert with the same name already exists
        if self.instance and self.instance.name == value:
            return value  # Allow the current instance to be updated

        if Concert.objects.filter(name=value).exists():
            raise serializers.ValidationError("A concert with this name already exists.")
        return value

class SeatingLayoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeatingLayout
        fields = '__all__'

    def validate(self, data):
        # Check if a seating layout for the same concert, section, and seat_number already exists
        if self.instance and self.instance.concert == data.get('concert') and self.instance.section == data.get('section') and self.instance.seat_number == data.get('seat_number'):
            return data  # Allow the current instance to be updated

        if SeatingLayout.objects.filter(concert=data['concert'], section=data['section'], seat_number=data['seat_number']).exists():
            raise serializers.ValidationError("This seating layout already exists.")
        return data

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

    def validate(self, data):
        # Check if required fields are present
        if not data.get('name'):
            raise serializers.ValidationError("Name is required.")

        if not data.get('email'):
            raise serializers.ValidationError("Email is required.")

        if not data.get('concert'):
            raise serializers.ValidationError("Concert is required.")

        if not data.get('seating_layout'):
            raise serializers.ValidationError("Seating layout is required.")

        # Check if a reservation for the same concert and seating_layout already exists
        if self.instance and self.instance.concert == data.get('concert') and self.instance.seating_layout == data.get('seating_layout'):
            return data  # Allow the current instance to be updated

        if Reservation.objects.filter(concert=data['concert'], seating_layout=data['seating_layout']).exists():
            raise serializers.ValidationError("This reservation already exists.")
        return data
