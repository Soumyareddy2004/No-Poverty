from django.shortcuts import render
from django.http import JsonResponse
from .models import Volunteer

def volun_home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('phone')
        age = request.POST.get('age')
        message = request.POST.get('message', '')

        if not name or not email or not mobile_number or not age:
            return JsonResponse({'error': 'All fields are required!'}, status=400)

        volunteer = Volunteer(
            name=name,
            email=email,
            mobile_number=mobile_number,
            age=age,
            message=message
        )
        volunteer.save()

        return JsonResponse({'message': 'Thank you for volunteering!'})

    return render(request, 'volun.html')
