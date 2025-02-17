import rasterio
import numpy as np
from PIL import Image
# from langsam import LangSAM

def segment_image_with_prompts(image_path, prompts):
    """
    Segments an image based on the provided prompts using LangSAM.

    Parameters:
        image_path (str): The path to the image file.
        prompts (list): A list of text prompts to guide segmentation.

    Returns:
        None: Saves the segmented output for each prompt.
    """
    # Initialize LangSAM
    langSAM = LangSAM()

    for prompt in prompts:
        # Read the image data using rasterio
        with rasterio.open(image_path) as src:
            image_data = src.read()

        # If the image is single-band, convert it to a 2D array
        if image_data.shape[0] == 1:
            image_np = image_data.squeeze()  # Remove the extra dimension
        else:
            image_np = np.transpose(image_data, (1, 2, 0))  # Reorder dimensions to (height, width, channels)

        # Convert the image to RGB if it's not already
        if image_np.shape[-1] != 3:
            image_np = np.stack((image_np,) * 3, axis=-1)  # Stack the grayscale image 3 times to create RGB

        # Convert the NumPy array to a PIL Image
        image_pil = Image.fromarray(image_np.astype(np.uint8))  # Ensure data type is uint8 for PIL

        # Continue with LangSAM prediction using the PIL Image
        langSAM.predict(
            image=image_pil,  # Pass the PIL Image object
            text_prompt=prompt,
            box_threshold=0.15,
            text_threshold=0.9,
        )

        # Show and save the segmented output
        langSAM.show_anns(
            cmap='Reds',
            add_boxes=False,
            alpha=0.5,
            title=f'{prompt}',
            blend=True,
            output=f'{prompt}_segmentation.tif'
        )


# Example usage:
image_path = './1.tif'  # Path to your image file
prompts = [
    "artificial structure",
    "construction",
    "man-made structure",
    "roof footprint",
    "building footprint",
    "regular shape building",
    "tall building",
    "low-rise building",
    "large building",
    "small building",
    "roof",
    "rooftop",
    "house",
    "house roof",
    "house rooftop",
    "building",
    "building roof",
    "building rooftop",
    "house rooftop footprint",
    "house roof footprint",
    "building rooftop footprint",
    "building roof footprint",
]




import requests
from django.shortcuts import render
import google.generativeai as genai
import os
from django.http import JsonResponse
import pandas as pd

# 🔹 Replace with your valid Google API keys
GEOCODING_API_KEY = 'AIzaSyDT8SH4ZwByMZndW5tlRccp6pcoEY31PFw'
STATIC_MAPS_API_KEY = 'AIzaSyDT8SH4ZwByMZndW5tlRccp6pcoEY31PFw'

# Load your CSV file
data = pd.read_csv('f0.csv')  # Replace with your actual CSV path

# Calculate the threshold (average) for each column except 'District'
threshold = data.drop(columns=['District code', 'State name', 'District name']).mean()

# Gemini AI Configuration
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_coordinates(address):
    """Fetch latitude and longitude using Google Geocoding API."""
    geocoding_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={GEOCODING_API_KEY}"

    try:
        response = requests.get(geocoding_url)
        data = response.json()

        if response.status_code == 200 and data['status'] == 'OK':
            lat = data['results'][0]['geometry']['location']['lat']
            lng = data['results'][0]['geometry']['location']['lng']
            return lat, lng
    except Exception as e:
        print(f"Error fetching coordinates: {e}")
    
    return None, None

def check_below_threshold(district):
    """Check which facilities are below threshold for a given district."""
    district = district.lower()
    district_data = data[data['District name'].str.lower() == district].drop(columns=['District code', 'State name', 'District name'])

    if district_data.empty:
        return []

    below_threshold_columns = [col for col in district_data.columns if district_data[col].iloc[0] < threshold[col]]
    return below_threshold_columns

def get_ai_suggestions(address):
    """Get AI suggestions for facilities below the threshold."""
    prompt = f"""
    Act as an evaluator and from the following facilities in a country are lagging:
    {address}
    For the following place, describe me about how the city is, how the houses are constructed and how the roads and electricity are. Give all in points. Please ensure you don't cross 200 words. 
    """

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text  # Get AI response
    except Exception as e:
        return f"Error: {str(e)}"

def map_view(request):
    """Render the map page and handle user input for location and district."""
    map_url_standard = None
    map_url_night = None
    ai_suggestions = None
    below_threshold_columns = []

    if request.method == 'POST':
        # Get the location for the map and district for AI suggestions
        address = request.POST.get('address')
        # district_name = request.POST.get('district')

        # Fetch coordinates for the address to display the map
        lat, lng = get_coordinates(address)

        if lat and lng:
            # Standard satellite map URL
            map_url_standard = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lng}&zoom=12&size=600x600&maptype=satellite&key={STATIC_MAPS_API_KEY}"

            # Night mode satellite map URL
            night_mode_style = [
                {"elementType": "geometry", "stylers": [{"color": "#212121"}]},
                {"elementType": "labels.icon", "stylers": [{"visibility": "off"}]},
                {"elementType": "labels.text.fill", "stylers": [{"color": "#757575"}]},
                {"elementType": "labels.text.stroke", "stylers": [{"color": "#212121"}]},
                {"featureType": "road", "elementType": "geometry", "stylers": [{"color": "#212121"}]},
                {"featureType": "water", "elementType": "geometry", "stylers": [{"color": "#000000"}]}
            ]
            night_mode_style_str = str(night_mode_style).replace("'", '"')
            map_url_night = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lng}&zoom=12&size=600x600&maptype=roadmap&key={STATIC_MAPS_API_KEY}&style={night_mode_style_str}"
            ai_suggestions = get_ai_suggestions(address)

    return render(request, 'map.html', {
        'map_url_standard': map_url_standard,
        'map_url_night': map_url_night,
        'ai_suggestions': ai_suggestions,
    })



