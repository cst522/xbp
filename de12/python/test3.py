import urllib.request
import json
import time

# OpenWeatherMap APIキーを取得してください
api_key = '2ac00926ab84ac46e5872e550aa4a2de'
city = 'Yokohama,JP'

def get_pressure():
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    
    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        pressure = data['main']['pressure']
        return pressure
    except urllib.error.URLError as e:
        print('気圧情報の取得に失敗しました。エラー:', e)
        return None

while True:
    pressure = get_pressure()
    
    if pressure is not None:
        if pressure <= 1007:
            print('気圧が1007hPa以下になりました。頭痛注意！')
    
    time.sleep(7200)  # 2時間待機
