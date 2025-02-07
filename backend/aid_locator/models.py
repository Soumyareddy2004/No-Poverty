from django.db import models

class WelfareScheme(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)  # City, State, etc.

    def __str__(self):
        return self.name

class JobOpening(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    job_type = models.CharField(max_length=50, choices=[('Tech', 'Tech'), ('Non-Tech', 'Non-Tech')])
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} at {self.company}"
