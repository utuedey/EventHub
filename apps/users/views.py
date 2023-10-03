#!/usr/bin/env python
"""
users/views.py
contains the user authentication system views
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from apps.users.forms import CustomUserCreationForm

def dashboard(request):
    """A sample dashboard to use the authentication system
    """
    return render(request, 'event_hub/index.html')

def register(request):
    """Handles registration form request
    """
    if request.method == "GET":
        return render(
            request, "registration/signup.html", # change template from register.html
            {'form': CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            user.save()
            login(request, user)
            return redirect(reverse("dashboard"))