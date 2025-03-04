import os
import pandas as pd
import google.generativeai as genai
from django.shortcuts import render
from django.http import JsonResponse

# Load CSV file
data = pd.read_csv('f0.csv')

# Calculate the threshold (average) for each column except 'District'
threshold = data.drop(columns=['District code', 'State name', 'District name']).mean()

# Gemini AI Configuration
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Function to check below threshold
def check_below_threshold(district):
    district = district.lower()
    district_data = data[data['District name'].str.lower() == district].drop(columns=['District code', 'State name', 'District name'])

    if district_data.empty:
        return []

    below_threshold_columns = [col for col in district_data.columns if district_data[col].iloc[0] < threshold[col]]
    return below_threshold_columns

# Function to get AI suggestions
def get_ai_suggestions(facilities):
    prompt = f"""
    Act as an evaluator and from the following facilities in a country are lagging:
    {facilities}
    Now do the following:
    1. Remove irrelevant facilities that do not affect poverty.
    2. Remove facilities related to any religion.
    3. Only display Effective Strategies to Improve Them and Reduce Poverty.
    
    I want the output to be structured only with the Effective strategies, don't print anything else.
    Print at least 5 effective strategies.
    """

    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt)
        return response.text  # Get AI response
    except Exception as e:
        return f"Error: {str(e)}"

# Django View
def ai_suggestions_view(request):
    if request.method == "POST":
        district_name = request.POST.get('district', '').strip()
        below_threshold_columns = check_below_threshold(district_name)

        if below_threshold_columns:
            suggestions = get_ai_suggestions(below_threshold_columns)
        else:
            suggestions = f"All values for {district_name} are above or equal to the threshold."

        return JsonResponse({"facilities": below_threshold_columns, "suggestions": suggestions})

    return render(request, "aisuggest/aisuggest.html")
