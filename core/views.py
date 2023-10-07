<<<<<<< HEAD
from django.conf import settings
import stripe
from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Category, Event, Payment, UserProfile, Ticket
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Add event
from .forms import AddEventForm

def generate_pdf_ticket(ticket):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename="{ticket.ticket_number}.pdf"'

    # Create a PDF document
    p = canvas.Canvas(response, pagesize=letter)
    p.drawString(100, 750, f"Ticket Number: {ticket.ticket_number}")
    # We will add more ticket details as needed

    # Save the PDF
    p.save()
    return response

def rent_venue(request):
    """View to add rent a venue"""
    return render(request, 'event_hub/rent-venue.html')

def purchase_ticket(request):
    """View to purchase ticket"""
    return render(request, 'event_hub/tickets.html')

def ticket_detail(request):
    """View to purchase ticket"""
    return render(request, 'event_hub/ticket-details.html')

def about(request):
    """the about page view"""
    return render(request, 'event_hub/about.html')

def contact_page(request):
    """the contact page view"""
    return render(request, 'event_hub/contact.html')

def add_event(request):
    if request.method == 'POST':
        form = AddEventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/ticket/")
    else:
         form = AddEventForm()
    return render(request, 'add_event.html', {'form': form})

class EventListView(ListView):
    """View to display a list of events"""
    model = Event
    template_name = 'event_hub/event_list.html'
    context_object_name = 'events'


class EventDetailView(DetailView):
    """View to display the details of an event"""
    model = Event
    template_name = 'eventhub/event-details.html'
    context_object_name = 'event'


@method_decorator(login_required, name='dispatch')
class UserProfileView(TemplateView):
    """View to display the user's profile"""
    template_name = 'user_profile.html'

    def get_context_data(self, **kwargs):
        """Add the user's profile to the context"""
        context = super().get_context_data(**kwargs)
        context['user_profile'] = UserProfile.objects.get(user=self.request.user)
        return context


@method_decorator(login_required, name='dispatch')
class EventRegistrationView(View):
    """View to register a user for an event"""
    def post(self, request, event_id):
        """Register a user for an event"""
        event = Event.objects.get(pk=event_id)

        # Check if the user is already registered for the event
        if Ticket.objects.filter(event=event, user=request.user).exists():
            # You might want to handle this case differently, e.g., show an error message
            return redirect('event-detail', pk=event_id)

        # Create a new ticket for the user
        ticket = Ticket(event=event, user=request.user)
        ticket.save()
=======
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
>>>>>>> 179b83e043e9ce0ea77fb80eed7d04a103eff56e

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
