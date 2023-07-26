import requests

"""
Built-in API request by city name:
https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
Parameters:
q, appid -> required, units, mode, lang -> optional
"""

def get_weather(city, api_key, units):
    api_url = "https://api.openweathermap.org/data/2.5/weather?"
    parameters = {
        "q": city,  # City name
        "appid": api_key,   # Your OpenWeatherMap API Key
        "units": units, # Metric, Imperial
    }
    response = requests.get(url=api_url, params=parameters)
    data = response.json()

    if units not in ["metric", "imperial"]:
        print("Enter Metric or Imperial!\n")
        exit()
    else:
        if units == "metric":
            temperature_symbol = "°C"
            speed_symbol = "m/s"
        else:
            temperature_symbol = "°F"
            speed_symbol = "mph"
    
    if response.status_code == 401:
        print("Invalid API key. Please see https://openweathermap.org/faq#error401 for more info.\n")
        exit()
    elif response.status_code == 404:
        print("City not found.\n")
        exit()
    elif response.status_code != 200:
        print(f"Error occured with the status code {response.status_code}")
        exit()

    city_name = data['name']
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    feels_like = data['main']['feels_like']
    wind_speed = data['wind']['speed']
    
    print(f"City: {city_name}")
    print(f"Temperature: {temperature}{temperature_symbol}")
    print(f"Description: {description}")
    print(f"Feels like: {feels_like}{temperature_symbol}")
    print(f"Wind Speed: {wind_speed} {speed_symbol}")

if __name__ == "__main__":
    api_key = input("Enter your OpenWeatherMap API key: ")
    city = input("Enter the City: ")
    units = input("Enter Units (Metric/Imperial): ").lower()

    get_weather(city, api_key, units)
