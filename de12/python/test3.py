import requests
from datetime import datetime

api_url = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"
weather_data = requests.get(api_url).json()
print(weather_data)