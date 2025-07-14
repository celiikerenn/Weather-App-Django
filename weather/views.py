import requests
import os
from dotenv import load_dotenv
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .models import City
from .forms import CityForm

load_dotenv()
API_KEY = os.getenv("API_KEY")

ICON_MAP = {
    'Clear': 'sun.svg',
    'Clouds': 'cloud.svg',
    'Rain': 'rain.svg',
    'Thunderstorm': 'storm.svg',
    'Snow': 'snow.svg',
    'Drizzle': 'drizzle.svg',
    'Mist': 'mist.svg',
    'Fog': 'fog.svg',
    'Haze': 'haze.svg',
    'Smoke': 'smoke.svg',
}

def home(request):
    form = CityForm()

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name']
            if not City.objects.filter(name__iexact=city_name).exists():
                form.save()

    cities = City.objects.all()
    weather_data = []


    for city in cities:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city.name}&appid={API_KEY}&units=metric&lang=en'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            icon_key = data['weather'][0]['main']
            custom_icon = ICON_MAP.get(icon_key, 'default.svg')

            weather = {
                'id': city.id,
                'city': city.name,
                'temp': data['main']['temp'],
                'description': data['weather'][0]['description'].capitalize(),
                "icon_url": f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"

            }
        else:
            weather = {
                'id': city.id,
                'city': city.name,
                'temp': 'N/A',
                'description': 'City not found'
            }

        weather_data.append(weather)

    return render(request, 'weather/home.html', {
        'form': form,
        'weather_data': weather_data
    })

def delete_city(request, city_id):
    city = get_object_or_404(City, id=city_id)
    city.delete()
    return redirect('home')

def delete_all_cities(request):
    City.objects.all().delete()
    return redirect('home')