"""
pat app URL Configuration
"""
from django.urls import path
from .views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]
