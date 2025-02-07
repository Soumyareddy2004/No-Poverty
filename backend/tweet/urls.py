from django.urls import path
from . import views  # Ensure you're importing from the same module

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('tweets/', views.tweet_list, name='tweet_list'),
    path('tweet/create/', views.tweet_create, name='tweet_create'),
    path('tweet/<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('tweet/<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    path('register/', views.register, name='register'),
]
