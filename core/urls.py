from django.urls import path
from . import views


urlpatterns = [
    path('show-events/', views.EventListView.as_view(), name='event-list'),
    # rent venue url
    path('rent-venue/', views.rent_venue, name='rent-venue'),
    # purchase ticket url
    path('tickets/', views.purchase_ticket, name='ticket'),
    # ticket_details url
    path('ticket_details/', views.ticket_detail, name='ticket-detail'),
    # about page url
    path('about/', views.about, name='about'),
    # contact page url 
    path('contact/', views.contact_page, name='contact'),
    # event registration url
    path('register_event/', views.add_event, name='add-event'),
    path('event-detail/', views.EventDetailView.as_view(), name='event-detail'), # event-detail/<int:pk>/
    path('profile/', views.UserProfileView.as_view(), name='user-profile'),
    path('events/<int:event_id>/register/', views.EventRegistrationView.as_view(), name='event-registration'),
    path('events/<int:event_id>/unregister/', views.EventUnregistrationView.as_view(), name='event-unregistration'),
    path('search/', views.EventSearchView.as_view(), name='event-search'),
    path('categories/<int:pk>/', views.EventCategoryView.as_view(), name='event-category'),
    path('api/categories/', views.AllCategoriesView.as_view(), name='all-categories'),
    path('tags/<int:pk>/', views.EventTagView.as_view(), name='event-tag'),
]
