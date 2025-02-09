import os
import requests
from django.shortcuts import render
from django.conf import settings

def get_location_data(location):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    
    prompt = (
        f"List NGOs, welfare schemes, and job openings available in {location}. "
        f"For each NGO, welfare scheme, or job opening, provide a description and the official website URL "
        f"as a clickable hyperlink (e.g., [Job Title](https://example.com))."
    )
    
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }
    
    headers = {"Content-Type": "application/json"}
    params = {"key": settings.GEMINI_API_KEY}

    response = requests.post(url, json=payload, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        response_text = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "No results found.")
        return response_text
    else:
        return f"Error {response.status_code}: {response.text}"

def aid_locator_view(request):
    result = ""
    if request.method == "POST":
        location = request.POST.get("location")
        if location:
            result = get_location_data(location)
    
    return render(request, "aidloc.html", {"result": result})


def job_opportunities_view(request):
    return render(request, "jobs.html")


def job_opportunities_view(request):
    job_results = ""
    if request.method == "POST":
        location = request.POST.get("location")
        if location:
            job_results = get_location_data(location)
    
    return render(request, "jobs.html", {"job_results": job_results})

