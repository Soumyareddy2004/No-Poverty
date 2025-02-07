from django.shortcuts import render
import requests
from django.conf import settings
import google.generativeai as genai
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

# Create your views here.
def empowerment_view(request):
    return render(request, 'empowerment.html')

def resilience_view(request):
    return render(request, 'resilience.html')

def policy_view(request):
    return render(request, 'policy.html')


genai.configure(api_key=settings.GEMINI_API_KEY)  # Store API key in settings.py


def get_ai_jobs(request):
    PROMPT = "Recommend top 5 job opportunities for individuals looking for employment in various sectors."

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(PROMPT)
        jobs = response.text.split("\n")  # Convert response into a list of jobs

        return JsonResponse({"jobs": jobs})
    
    except Exception as e:
        return JsonResponse({"jobs": ["Error fetching job recommendations:", str(e)]})
    
def get_ai_crisis_help(request):
    PROMPT = "Provide guidance for someone seeking emergency support during a crisis."

    response = genai.chat(messages=[{"role": "user", "content": PROMPT}])

    if response:
        return JsonResponse({"response": response.text})
    else:
        return JsonResponse({"response": "AI support is currently unavailable."})