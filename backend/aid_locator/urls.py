# # aid_locator/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('aid_locator/', views.get_aid_locator, name='aid_locator'),
# ]
# aid_locator/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.aid_locator, name='aid_locator'),  # This handles the GET and POST requests
# ]


from django.urls import path
from .views import aid_locator_view

urlpatterns = [
    path('', aid_locator_view, name='aidloc'),  # If template uses 'aidloc'
  # Make sure this matches the template
]


