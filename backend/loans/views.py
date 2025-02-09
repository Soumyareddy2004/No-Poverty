from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import LoanApplication
from .forms import LoanApplicationForm

def loans_home(request):
    return render(request, "loans.html")

def check_eligibility(request):
    if request.method == "POST":
        age = int(request.POST.get('age', 0))
        business_idea = request.POST.get('business_idea', '')

        if age >= 18 and business_idea:
            return JsonResponse({"status": "Eligible", "message": "You are eligible for a microloan!"})
        else:
            return JsonResponse({"status": "Not Eligible", "message": "You must be at least 18 years old and provide a business idea."})

    return redirect('loans:loans_home')

def apply_loan(request):
    if request.method == "POST":
        form = LoanApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your loan application has been submitted successfully!")
            return redirect('loans:loans_home')  # ✅ Redirect after successful submission
        else:
            messages.error(request, "There was an error in your application. Please check your details.")

    return redirect('loans:loans_home')  # Redirect if not a POST request
