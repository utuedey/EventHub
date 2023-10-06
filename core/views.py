from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from .models import Tag, Event, UserProfile, Payment, Ticket, Location, Category
from .serializers import (
    TagSerializer,
    EventSerializer,
    UserProfileSerializer,
    PaymentSerializer,
    TicketSerializer,
    LocationSerializer,
    CategorySerializer
)

class HomeView(TemplateView):
    template_name = 'core/landingpage.html' #'event_hub/index.html'

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class EventRegistrationView(APIView):
    def post(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        user = request.user

        # Check if the user is already registered for the event
        if Ticket.objects.filter(event=event, user=user).exists():
            return Response({'detail': 'You are already registered for this event.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if there are available tickets
        if event.ticket_available <= 0:
            return Response({'detail': 'No available tickets for this event.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new ticket for the user
        ticket = Ticket(event=event, user=user)
        ticket.save()

        # Decrease the available ticket count for the event
        event.ticket_available -= 1
        event.save()

        # Serialize the ticket data for the response
        serializer = TicketSerializer(ticket)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EventDeregistrationView(APIView):
    def post(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        user = request.user

        # Check if the user is registered for the event
        try:
            ticket = Ticket.objects.get(event=event, user=user)
        except Ticket.DoesNotExist:
            return Response({'detail': 'You are not registered for this event.'}, status=status.HTTP_400_BAD_REQUEST)

        # Mark the ticket as invalid
        ticket.is_valid = False
        ticket.save()

        # Increase the available ticket count for the event
        event.ticket_available += 1
        event.save()

        return Response({'detail': 'Successfully deregistered from the event.'})


class AboutView(TemplateView):
    template_name = 'event_hub/about.html'

class ContactView(TemplateView):
    template_name = 'event_hub/contact.html'
