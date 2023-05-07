import requests

class WeatherAPIClient:
    BASE_URL = "http://api.weatherapi.com/v1"
    API_KEY = "927f7fc8a8d34c738ac120118230205"
    
    def get_current_temperature(self, city):
        url = f"{self.BASE_URL}/current.json?key={self.API_KEY}&q={city}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data["current"]["temp_c"]
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
    
    def get_temperature_after(self, city, days, hour=None):
        url = f"{self.BASE_URL}/forecast.json?key={self.API_KEY}&q={city}&days={days}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if hour:
                return data["forecast"]["forecastday"][0]["hour"][hour]["temp_c"]
            else:
                return data["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
    
    def get_lat_and_long(self, city):
        url = f"{self.BASE_URL}/forecast.json?key={self.API_KEY}&q={city}&days=1"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data["location"]["lat"], data["location"]["lon"]
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")

client = WeatherAPIClient()

temperature = client.get_temperature_after("London", 3, hour=15)
if temperature:
    print(f"The temperature in London in 3 days at 3pm will be {temperature}°C.")

lat_long = client.get_lat_and_long("London")
if lat_long:
    lat, long = lat_long
    print(f"The latitude and longitude for London are {lat}, {long}.")
