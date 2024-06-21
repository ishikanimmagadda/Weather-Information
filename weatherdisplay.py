import requests

api_key = 'b02c752e95bc925d00ba424a7f1eeebc'

city = input("Enter a city name: ")

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

#successful response 
if response.status_code == 200: 
    #dictionary 
    weatherData = response.json()

    maintemperature = weatherData['main']['temp']
    maintempCelsius = maintemperature - 273.15

    feelsliketemp = weatherData ['main']['feels_like']
    feelslikeCelsius = feelsliketemp - 273.15

    windSpeed = weatherData['wind']['speed']

    description = weatherData['weather'][0]['description']

    print("Temperature: " + str(maintempCelsius) + "C")
    print("Feels Like: " + str(feelslikeCelsius) + "C")
    print("Wind Speed: " + str(windSpeed))
    print("Description: " + str(description))
else: 
    print("error")
