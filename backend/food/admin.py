from django.contrib import admin
from .models import FoodDonation

@admin.register(FoodDonation)
class FoodDonationAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'pickup_time', 'created_at')
    search_fields = ('email', 'phone', 'pickup_time')
    list_filter = ('created_at',)