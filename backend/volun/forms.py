from django import forms
from .models import Volunteer

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['name', 'email', 'mobile_number', 'age', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'mobile_number': forms.TextInput(attrs={'placeholder': 'Your Mobile Number'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Your Age'}),
            'message': forms.Textarea(attrs={'placeholder': 'Why do you want to volunteer?', 'rows': 4}),
        }
