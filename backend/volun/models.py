from django.db import models

class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    age = models.IntegerField()
    message = models.TextField(blank=True, null=True)
    date_registered = models.DateTimeField(auto_now_add=True)  # Automatically set on creation

    def __str__(self):
        return self.name
