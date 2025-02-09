from django.contrib import admin
from .models import Volunteer

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile_number', 'age', 'date_registered')
    search_fields = ('name', 'email')
