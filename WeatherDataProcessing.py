import urllib.request
import json

with open('Cities.txt', 'r', encoding='utf-8-sig') as file:
    cities = file.read()
cities = cities.rstrip()
cities = cities.split('\n')

file.close()
WeatherData = []

for city in cities:
  url = f"https://wttr.in/{city}?format=j1"
  request = urllib.request.Request(url)
  with urllib.request.urlopen(request) as response:
    json_data = json.loads(response.read().decode('utf-8'))
    WeatherData.append({
        "City": json_data["nearest_area"][0]["areaName"][0]["value"],
        "Country": json_data["nearest_area"][0]["country"][0]["value"],
        "Current_temp_C" : json_data["current_condition"][0]['temp_C']})

for data in WeatherData:
  print(f"{data["City"]}, {data["Country"]} {'+' if int(data["Current_temp_C"]) > 0 else ''}{data["Current_temp_C"]} {chr(176)}C")

countries = dict()

for data in WeatherData:
  if data["Country"] not in countries:
    countries[data["Country"]] = []
  countries[data["Country"]].append(int(data["Current_temp_C"]))

for country, temps in countries.items():
  avg = sum(temps) / len(temps)
  mint = min(temps)
  maxt = max(temps)
  print(f"{country} - {len(temps)} cities, avg: {'+' if avg > 0 else ''}{avg} {chr(176)}C, min: {'+' if mint > 0 else ''}{mint} {chr(176)}C, max: {'+' if maxt > 0 else ''}{maxt} {chr(176)}C")