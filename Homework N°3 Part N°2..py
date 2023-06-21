# Federico Teijeiro.
# June 12, 2023.
# Homework N°3 Part N°2.

# What is the URL to the documentation?
#https://www.weatherapi.com/docs/

# Make a request for the current weather where you are born, or somewhere you've lived.
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("api_key")
import requests
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=Buenos Aires&aqi=no"
response = requests.get(url)
data = response.json()
print(data)
print("")

# Print out the country this location is in.
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=Buenos Aires&aqi=no"
response = requests.get(url)
data = response.json()
print(data["location"]["country"])
print("")

# Print out the difference between the current temperature and how warm it feels. Use "It feels ___ degrees colder" or "It feels ___ degrees warmer," 
# not negative numbers.
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=Buenos Aires&aqi=no"
response = requests.get(url)
data = response.json()
if data["current"]["temp_c"] > data["current"]["feelslike_c"]:
  colder = data["current"]["temp_c"] - data["current"]["feelslike_c"]
  print("It feels", round(colder, 2), "degrees colder")
elif data["current"]["temp_c"] < data["current"]["feelslike_c"]:
  warmer = data["current"]["temp_c"] - data["current"]["feelslike_c"]
  print("It feels", round(warmer, 2), "degrees colder")
else:
  print("It feels like the temperature.")  
print("")

# What's the current temperature at Heathrow International Airport? Use the airport's IATA code to search.
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=LHR&aqi=no"
response = requests.get(url)
data = response.json()
print(data["current"]["temp_c"])
print("")

# What URL would I use to request a 3-day forecast at Heathrow?
url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q=LHR&days=3&aqi=no&alerts=no"
response = requests.get(url)
data = response.json()

# Print the date of each of the 3 days you're getting a forecast for.
url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q=LHR&days=3&aqi=no&alerts=no"
response = requests.get(url)
data = response.json()
for forecast in data["forecast"]["forecastday"]: 
  print(forecast["date"])
print("")

# Print the maximum temperature of each of the days.
url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q=LHR&days=3&aqi=no&alerts=no"
response = requests.get(url)
data = response.json()
for max_temp in data["forecast"]["forecastday"]:
  print(max_temp["date"])
  print(max_temp["day"]["maxtemp_c"])
print("")

# Print only the day with the highest maximum temperature.
url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q=LHR&days=3&aqi=no&alerts=no"
response = requests.get(url)
data = response.json()
for max_temp in data["forecast"]["forecastday"]:
  print(max_temp["date"])
  print(max_temp["day"]["maxtemp_c"])
print("")
max_temp3d = {}
for day_max in data["forecast"]["forecastday"]:
  max_temp3d[day_max["date"]] = day_max["day"]["maxtemp_c"]
  print(max_temp3d)
print("")
print(max(max_temp3d, key=max_temp3d.get), max(max_temp3d.values()))