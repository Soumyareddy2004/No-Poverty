from django.urls import path
from .views import ai_suggestions_view

urlpatterns = [
    path('ai-suggestions/', ai_suggestions_view, name='ai_suggestions'),
]
