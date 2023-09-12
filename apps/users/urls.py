#!/usr/bin/env python
"""
users/urls.py
contains urls for users authentication system
"""

from django.urls import path, include
from .views import dashboard, register

urlpatterns = [
    # django's authentication system url
    path('accounts/', include('django.contrib.auth.urls')),
    path('', dashboard, name='dashboard'),
    path('register', register, name='register'),
]
