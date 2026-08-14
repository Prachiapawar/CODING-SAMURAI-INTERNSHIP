import requests

api_key = "YOUR_API_KEY"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("\nWeather Details")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Weather:", data["weather"][0]["description"])
        print("Humidity:", data["main"]["humidity"], "%")
        print("Wind Speed:", data["wind"]["speed"], "m/s")

    else:
        print("City not found. Please check the city name.")

except requests.exceptions.RequestException:
    print("Unable to connect to the weather service.")
