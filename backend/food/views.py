from django.shortcuts import render, redirect
from .forms import FoodDonationForm

def donate_food(request):
    if request.method == 'POST':
        form = FoodDonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = FoodDonationForm()
    return render(request, 'food_donation.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')  # Create success.html in templates folder
