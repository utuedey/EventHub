from django.conf import settings
import stripe
from django.shortcuts import redirect
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Category, Event, Payment, UserProfile, Ticket
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


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


class EventListView(ListView):
    """View to display a list of events"""
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'


class EventDetailView(DetailView):
    """View to display the details of an event"""
    model = Event
    template_name = 'event_detail.html'
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

        return redirect('event-detail', pk=event_id)

# THIS VIEW WILL BE USED, IT WILL REPLACE THE ABOVE VIEW, THE ABOVE VIEW IS FOR INITIAL TESTING
# @method_decorator(login_required, name='dispatch')
# class EventRegistrationView(View):
#     def post(self, request, event_id):
#         event = Event.objects.get(pk=event_id)
#         user = request.user
#         ticket_price = event.price

#         # Create a payment intent with Stripe
#         try:
#             stripe.api_key = settings.STRIPE_API_KEY
#             payment_intent = stripe.PaymentIntent.create(
#                 amount=int(ticket_price * 100),  # Amount in cents
#                 currency='usd',
#             )

#             # Create a payment record
#             payment = Payment.objects.create(
#                 event=event,
#                 user=user,
#                 amount=ticket_price,
#                 payment_intent_id=payment_intent.id,
#             )
#             payment.save()

#             return JsonResponse({'client_secret': payment_intent.client_secret})

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)



@method_decorator(login_required, name='dispatch')
class EventUnregistrationView(View):
    """View to unregister a user from an event"""
    def post(self, request, event_id):
        """Unregister a user from an event"""
        event = Event.objects.get(pk=event_id)

        # Check if the user is registered for the event
        try:
            ticket = Ticket.objects.get(event=event, user=request.user)
        except Ticket.DoesNotExist:
            # User is not registered, handle this case accordingly
            return redirect('event-detail', pk=event_id)

        ticket.delete()

        return redirect('event-detail', pk=event_id)


class EventSearchView(View):
    """View to retrieve all events matching a search query as JSON"""
    def get(self, request):
        """Return a list of all events matching a search query as JSON"""
        # Get the search query from the URL's GET parameters
        search_query = self.request.GET.get('q')

        # Implement event search and filtering logic
        queryset = Event.objects.all()

        if search_query:
            # Filter events based on the search query (customize this logic as needed)
            queryset = queryset.filter(title__icontains=search_query)

        # Serialize the queryset to JSON
        events = [{'title': event.title, 'description': event.description} for event in queryset]

        # Create a JSON response
        response_data = {'events': events}

        return JsonResponse(response_data)


class EventCategoryView(View):
    """View to retrieve all events with a specific category as JSON"""
    def get(self, request, pk):
        """Return a list of all events with a specific category as JSON"""
        # Implement event category filtering logic
        queryset = Event.objects.filter(category_id=pk)

        # Serialize the queryset to JSON
        events = [{'title': event.title, 'description': event.description} for event in queryset]

        # Create a JSON response
        response_data = {'events': events}

        return JsonResponse(response_data)


class EventTagView(View):
    """View to retrieve all events with a specific tag as JSON"""
    def get(self, request, pk):
        """Return a list of all events with a specific tag as JSON"""
        # Implement event tag filtering logic
        queryset = Event.objects.filter(tags__pk=pk)

        # Serialize the queryset to JSON
        events = [{'title': event.title, 'description': event.description} for event in queryset]

        # Create a JSON response
        response_data = {'events': events}

        return JsonResponse(response_data)

class AllCategoriesView(View):
    """View to retrieve all categories as JSON"""
    def get(self, request):
        """Return a list of all categories as JSON"""
        # Retrieve all categories
        categories = Category.objects.all().values()

        # Convert to a list and return as JSON
        categories_list = list(categories)

        # Create a JSON response
        response_data = {'categories': categories_list}

        return JsonResponse(response_data)
