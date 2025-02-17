# models.py
from django.db import models

class FoodDonation(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    pickup_time = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.pickup_time}"
