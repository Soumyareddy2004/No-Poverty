# urls.py
from django.urls import path
from .views import aid_locator_view, job_opportunities_view  # Import job_opportunities_view
urlpatterns = [
    path('', aid_locator_view, name='aidloc'),  # Existing aid locator
    path('jobs/', job_opportunities_view, name='job_opportunities'),
]
