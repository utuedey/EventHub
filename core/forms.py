from django import forms
from .models import Ticket

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = []  # You can define fields here if needed
