from django.urls import path, include
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from .views import (
    LocationViewSet,
    CategoryViewSet,
    TagViewSet,
    EventViewSet,
    UserProfileViewSet,
    PaymentViewSet,
    TicketViewSet,
    EventRegistrationView,
    EventDeregistrationView,
    HomeView,
    AboutView,
    ContactView,
    EventDetailView,
    TicketListView,
    IndexView
)

# Create a SimpleRouter for the main resources
router = DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'events', EventViewSet)
router.register(r'profiles', UserProfileViewSet)
router.register(r'payments', PaymentViewSet)

event_router = NestedDefaultRouter(router, r'events', lookup='event')
event_router.register(r'tickets', TicketViewSet, basename='event-tickets')

router_urls = router.urls + event_router.urls

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('tickets/', TicketListView.as_view(), name='ticket-list'),
    path('index/', IndexView.as_view(), name='index'),
    path('api/', include(router_urls)),
    path('events/<int:event_id>/registration/', EventRegistrationView.as_view(), name='event-registration'),
    path('events/<int:event_id>/deregistration/', EventDeregistrationView.as_view(), name='event-deregistration'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]
