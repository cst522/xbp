# Code InportError になってrequestが使えなかった
#urllib.request は URLs (Uniform Resource Locators) を取得するための Python モジュールである
import urllib.request
import json

# OpenWeatherMap APIキーを取得して入力
api_key = '2ac00926ab84ac46e5872e550aa4a2de'
# 取得したい地域のcityコードを入力
city = 'Yokohama,JP'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

try:
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode('utf-8'))
    
    pressure = data['main']['pressure']
    
    print(f'横浜の気圧: {pressure} hPa')
except urllib.error.URLError as e:
    print('気圧情報の取得に失敗しました。エラー:', e)
if pressure <= 1007:
            print('低気圧になりました。頭痛注意！薬を飲みましょう')
