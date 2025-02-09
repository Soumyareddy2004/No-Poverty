from django.urls import path
from .views import loans_home, apply_loan, check_eligibility

app_name = 'loans'  # ✅ Define namespace

urlpatterns = [
    path('', loans_home, name='loans_home'),
    path('apply-loan/', apply_loan, name='apply_loan'),
    path('check-eligibility/', check_eligibility, name='check_eligibility'),
]
