# from django.shortcuts import render, redirect
# from django.contrib import messages  # Import messages for user feedback
# from .forms import CityForm
# from .models import City
# import requests  # Make sure you import requests to handle API calls

# # Define the weather API URL
# API_KEY = 'e7baccdc203891ff18b7f19b5833f2db'  # Your actual API key
# BASE_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

# def home(request):
#     return render(request, 'header.html')

# def weather(request):
#     if request.method == 'POST':
#         form = CityForm(request.POST)
#         if form.is_valid():
#             NCity = form.cleaned_data['name']
#             CCity = City.objects.filter(name=NCity).count()

#             if CCity == 0:  # If the city does not exist in the database
#                 res = requests.get(BASE_URL.format(NCity, API_KEY)).json()  # Pass the API key correctly
#                 if res['cod'] == 200:  # If the city is found
#                     form.save()  # Save the new city to the database
#                     messages.success(request, f"{NCity} added successfully!")
#                 else:
#                     messages.error(request, "City does not exist!")
#             else:
#                 messages.error(request, "City already exists!")

#             return redirect('weather')  # Redirect to the weather view (or another view)
#     else:
#         form = CityForm()
#         cities=City.objects.all()
#         data=[]
#         for city in cities:
#             res=request.get(url.format(city)).json()
#             city_weather={
#                 'city':city,
#                 'temperature':res['main']['temp'],
#                 'description':res['weather'][0]['description'],
#                 'country':res['weather'][0]['icon'],
#             }
#             data.append(city_weather)
#     context={'data':data,'form':form}
#     return render(request, 'weatherapp.html',context)

# def delete_city(request,CName):
#     City.objects.get(name=CName).delete()
#     messages.success(request," "+CName+"removed sucessfully")
#     return redirect('weather')
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CityForm
from .models import City
import requests

# Define the weather API URL
API_KEY = 'e7baccdc203891ff18b7f19b5833f2db'  # Your actual API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

def home(request):
    return render(request, 'header.html')

def weather(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            NCity = form.cleaned_data['name']
            CCity = City.objects.filter(name=NCity).count()

            if CCity == 0:  # If the city does not exist in the database
                res = requests.get(BASE_URL.format(NCity, API_KEY)).json()
                if res['cod'] == 200:  # If the city is found
                    form.save()  # Save the new city to the database
                    messages.success(request, f"{NCity} added successfully!")
                else:
                    messages.error(request, "City does not exist!")
            else:
                messages.error(request, "City already exists!")

            return redirect('weather')  # Redirect to the weather view (or another view)
    else:
        form = CityForm()
        cities = City.objects.all()
        data = []
        for city in cities:
            res = requests.get(BASE_URL.format(city.name, API_KEY)).json()
            if res['cod'] == 200:  # Check if the response is valid
                city_weather = {
                    'city': city.name,  # Store city name
                    'temperature': res['main']['temp'] - 273.15,  # Convert from Kelvin to Celsius
                    'description': res['weather'][0]['description'],
                    'icon': res['weather'][0]['icon'],
                    'country': res['sys']['country'],  # Get country code
                }
                data.append(city_weather)

        context = {'data': data, 'form': form}
    return render(request, 'weatherapp.html', context)

def delete_city(request, CName):
    City.objects.get(name=CName).delete()
    messages.success(request, f"{CName} removed successfully")
    return redirect('weather')
