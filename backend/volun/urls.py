from django.urls import path
from . import views

urlpatterns = [
    path('', views.volun_home, name='volun'),  # Home page for volunteer form
]
