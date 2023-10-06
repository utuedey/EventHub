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
    EventDetailView
)

# Create a SimpleRouter for the main resources
router = DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'events', EventViewSet)
router.register(r'profiles', UserProfileViewSet)
router.register(r'payments', PaymentViewSet)

# Create a NestedDefaultRouter for Tickets under Events
event_router = NestedDefaultRouter(router, r'events', lookup='event')
event_router.register(r'tickets', TicketViewSet, basename='event-tickets')

router_urls = router.urls + event_router.urls

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('api/', include(router_urls)),
    path('events/<int:event_id>/registration/', EventRegistrationView.as_view(), name='event-registration'),
    path('events/<int:event_id>/deregistration/', EventDeregistrationView.as_view(), name='event-deregistration'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]
    

# from django.urls import path
# from . import views


# urlpatterns = [
#     path('', views.EventListView.as_view(), name='event-list'),
#     path('events/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
#     path('show-events/', views.EventListView.as_view(), name='event-list'),
#     # rent venue url
#     path('rent-venue/', views.rent_venue, name='rent-venue'),
#     # purchase ticket url
#     path('tickets/', views.purchase_ticket, name='ticket'),
#     # ticket_details url
#     path('ticket_details/', views.ticket_detail, name='ticket-detail'),
#     # about page url
#     path('about/', views.about, name='about'),
#     # contact page url 
#     path('contact/', views.contact_page, name='contact'),
#     path('event-detail/', views.EventDetailView.as_view(), name='event-detail'), # event-detail/<int:pk>/
#     path('profile/', views.UserProfileView.as_view(), name='user-profile'),
#     path('events/<int:event_id>/register/', views.EventRegistrationView.as_view(), name='event-registration'),
#     path('events/<int:event_id>/unregister/', views.EventUnregistrationView.as_view(), name='event-unregistration'),
#     path('search/', views.EventSearchView.as_view(), name='event-search'),
#     path('categories/<int:pk>/', views.EventCategoryView.as_view(), name='event-category'),
#     path('categories/', views.AllCategoriesView.as_view(), name='all-categories'),
#     path('tags/<int:pk>/', views.EventTagView.as_view(), name='event-tag'),
# ]
