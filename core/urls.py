from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventListView.as_view(), name='event-list'),
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
    path('profile/', views.UserProfileView.as_view(), name='user-profile'),
    path('events/<int:event_id>/register/', views.EventRegistrationView.as_view(), name='event-registration'),
    path('events/<int:event_id>/unregister/', views.EventUnregistrationView.as_view(), name='event-unregistration'),
    path('search/', views.EventSearchView.as_view(), name='event-search'),
    path('categories/<int:pk>/', views.EventCategoryView.as_view(), name='event-category'),
    path('categories/', views.AllCategoriesView.as_view(), name='all-categories'),
    path('tags/<int:pk>/', views.EventTagView.as_view(), name='event-tag'),
]
