from django import forms
from .models import Ticket, Event

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = []  # You can define fields here if needed


class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
    
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'contact-form',
                'placeholder': "Enter the title of the event",
            }),

            'description': forms.Textarea(attrs={
                'class': 'contact-form'
            }),

            'organizer': forms.Select(attrs={
                'class': 'contact-form'
            }),

            'category': forms.Select(attrs={
                'class': 'contact-form'
            }),

            'location': forms.Select(attrs={
                'class': 'contact-form'
            }),

            'date_time': forms.DateTimeInput(attrs={
                'class': 'contact-form',
                'placeholder': "Enter the start date and time of the event"
            }),

            'registration_deadline': forms.DateTimeInput(attrs={
                'class': 'contact-form',
                 'placeholder': "Enter the event registration deadline"
            }),

            'tags': forms.Select(attrs={
                'class': 'contact-form'
            }),
        }
