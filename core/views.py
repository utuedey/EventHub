from django.shortcuts import redirect
from django.views import View
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Category, Event, UserProfile, Ticket


class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'


class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'
    context_object_name = 'event'


@method_decorator(login_required, name='dispatch')
class UserProfileView(TemplateView):
    template_name = 'user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile'] = UserProfile.objects.get(user=self.request.user)
        return context


@method_decorator(login_required, name='dispatch')
class EventRegistrationView(View):
    def post(self, request, event_id):
        event = Event.objects.get(pk=event_id)

        # Check if the user is already registered for the event
        if Ticket.objects.filter(event=event, user=request.user).exists():
            # You might want to handle this case differently, e.g., show an error message
            return redirect('event-detail', pk=event_id)

        # Create a new ticket for the user
        ticket = Ticket(event=event, user=request.user)
        ticket.save()

        return redirect('event-detail', pk=event_id)

@method_decorator(login_required, name='dispatch')
class EventUnregistrationView(View):
    def post(self, request, event_id):
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
    def get(self, request):
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
    def get(self, request, pk):
        # Implement event category filtering logic
        queryset = Event.objects.filter(category_id=pk)

        # Serialize the queryset to JSON
        events = [{'title': event.title, 'description': event.description} for event in queryset]

        # Create a JSON response
        response_data = {'events': events}

        return JsonResponse(response_data)


class EventTagView(View):
    def get(self, request, pk):
        # Implement event tag filtering logic
        queryset = Event.objects.filter(tags__pk=pk)

        # Serialize the queryset to JSON
        events = [{'title': event.title, 'description': event.description} for event in queryset]

        # Create a JSON response
        response_data = {'events': events}

        return JsonResponse(response_data)

class AllCategoriesView(View):
    def get(self, request):
        # Retrieve all categories
        categories = Category.objects.all().values()

        # Convert to a list and return as JSON
        categories_list = list(categories)

        # Create a JSON response
        response_data = {'categories': categories_list}

        return JsonResponse(response_data)
