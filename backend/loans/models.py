from django.db import models

class LoanApplication(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)  # ✅ Match field name
    email = models.EmailField()
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)  # ✅ Match field name
    business_idea = models.TextField()
    status = models.CharField(max_length=20, default="Pending")
    timestamp = models.DateTimeField(auto_now_add=True)  # Track submission time

    def __str__(self):
        return f"{self.name} - {self.loan_amount}"
