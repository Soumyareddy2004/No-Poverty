from django.urls import path
from . import views  
from .views import donate
urlpatterns = [
    path('', views.donate, name='donate'),
]


