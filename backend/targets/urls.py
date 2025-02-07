from django.urls import path
from .views import empowerment_view, resilience_view, policy_view

urlpatterns = [
    path('empowerment/', empowerment_view, name='empowerment'),
    path('resilience/', resilience_view, name='resilience'),
    path('policy/', policy_view, name='policy'),
]