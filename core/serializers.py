from rest_framework import serializers
from .models import Location, Category, Tag, Event, UserProfile, Payment, Ticket


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'city', 'state', 'address' 'address', 'latitude', 'longitude']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
    

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class SimpleLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['city', 'state', 'address']


class SimpleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class SimpleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class EventSerializer(serializers.ModelSerializer):
    location = SimpleLocationSerializer()
    category = SimpleCategorySerializer()
    tags = SimpleTagSerializer(many=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'organizer', 'category', 'location', 'date_time', 'ticket_price', 'image', 'capacity', 'registration_deadline', 'tags']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'profile_picture', 'bio']


class PaymentSerializer(serializers.ModelSerializer):
    """Serializer for Payment objects"""
    class Meta:
        """Meta class for PaymentSerializer"""
        model = Payment
        fields = ['id', 'user', 'event', 'amount', 'payment_intent_id', 'payment_date']



class TicketSerializer(serializers.ModelSerializer):
    """Serializer for Ticket objects"""
    class Meta:
        """Meta class for TicketSerializer"""
        model = Ticket
        fields = ['id', 'user', 'event', 'ticket_type', 'quantity', 'payment']