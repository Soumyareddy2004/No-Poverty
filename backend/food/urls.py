from django.urls import path
from .views import donate_food, success_view

urlpatterns = [
    path('donate/', donate_food, name='donate_food'),
    path('success/', success_view, name='success'),  # Add this line
]
