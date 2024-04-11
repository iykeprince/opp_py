import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather(city = "Lagos"):

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()
  


    return weather_data

if  __name__ == "__main__":
    print('\n****Get Current Weather Conditions ****')
    city = input("\nPlease enter your city:\n")

    weather_data = get_current_weather(city)
    
    print(f'\nCurrent weather for {weather_data["name"]}, {weather_data["sys"]["country"]}')
    print(f'\nThe temp is {weather_data["main"]["temp"]}')
    print(f'\nThe temp is {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"]}.')