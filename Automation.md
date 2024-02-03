


import requests

def get_health_information(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # You can change the units as needed
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']

            health_info = {
                'city': city,
                'temperature': temperature,
                'humidity': humidity,
                'description': description
            }

            return health_info
        else:
            print(f"Error: {data['message']}")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    city_name = input("Enter the city name: ")
    api_key = input("Enter your OpenWeatherMap API key: ")

    health_info = get_health_information(city_name, api_key)

    if health_info:
        print(f"\nHealth Information for {health_info['city']}:")
        print(f"Temperature: {health_info['temperature']}°C")
        print(f"Humidity: {health_info['humidity']}%")
        print(f"Description: {health_info['description']}")
    else:
        print("Failed to retrieve health information.")

