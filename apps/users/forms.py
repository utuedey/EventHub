#!/usr/bin/env python
"""
users/forms.py
contain custom user creation form
"""
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    """A custom user creation form with additional email form
    """
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)
