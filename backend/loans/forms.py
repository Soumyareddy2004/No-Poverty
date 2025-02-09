from django import forms
from .models import LoanApplication

class LoanApplicationForm(forms.ModelForm):
    class Meta:
        model = LoanApplication
        fields = ['name', 'phone_number', 'email', 'loan_amount', 'business_idea']  # ✅ Use correct field names
