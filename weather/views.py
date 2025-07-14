import requests
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .models import City
from .forms import CityForm

API_KEY = '2a4e05c70693395329f7ef9e1239fef4'

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
            weather = {
                'id': city.id,
                'city': city.name,
                'temp': data['main']['temp'],
                'description': data['weather'][0]['description'].capitalize(),
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