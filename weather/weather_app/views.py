import requests
from django.shortcuts import render

# Create your views here.

def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=f0d9362414d6e2bada18d7816f23464a'
    city = 'Las Vegas'

    r = requests.get(url.format(city)).json()

    city_weather = {
        'city': city,
        'temperature': r["main"]['temp'],
        'description': r["weather"][0]["description"],
        'icon': r['weather'][0]['icon'],
    }

    context = {'city_weather': city_weather}
    return render(request, 'weather_app/weather.html', context)
