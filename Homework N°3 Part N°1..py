# Federico Teijeiro.
# June 12, 2023.
# Homework N°3 Part N°1.

# What is the URL to the documentation?
import requests
url = "http://pokeapi.co/api/v2"
response = requests.get(url)
print(response)
print(response.text)
print("")

# What pokemon has the ID of 55?
# How tall is that pokemon?
url = "https://pokeapi.co/api/v2/pokemon/55"
response = requests.get(url).json()
print(response['name'])
print(response['height'])
print("")

# How many versions of Pokemon games have been released?
url = "https://pokeapi.co/api/v2/version/"
response = requests.get(url).json()
print(response)
print("")

url = 'https://pokeapi.co/api/v2/version/'
version_response = requests.get(url)
version_data = version_response.json()
print("There are", version_data['count'], "versions in Pokemon.")
print ("")

# Print out the name of every electric-type pokemon.
url = "https://pokeapi.co/api/v2/type/electric"
response = requests.get(url)
data = response.json()
print(data.keys())
print ("")
for poke_name in data["pokemon"]:
  print(poke_name)
print ("")

url = "https://pokeapi.co/api/v2/type/electric"
response = requests.get(url)
data = response.json()
print(data.keys())
print ("")
for poke in data ["pokemon"]:
  print(poke ["pokemon"] ["name"])
print ("")

# What are electric-type Pokemon called in the Korean version of the game? (i.e. what do they call electric-type pokemon in Korean if not "electric")
url = "https://pokeapi.co/api/v2/type/electric"
response = requests.get(url)
data = response.json()
poke_lang = {}
for language in data["names"]:
  poke_lang[language["language"]["name"]] = language["name"]
print(poke_lang["ko"])
print ("")

# Who has a higher speed stat, Eevee or Pikachu?
url = "https://pokeapi.co/api/v2/pokemon/pikachu"
response = requests.get(url)
data1 = response.json()
print(data1["stats"][5]["base_stat"])
pika_speed = data1["stats"][5]["base_stat"]

url = "https://pokeapi.co/api/v2/pokemon/eevee"
response = requests.get(url)
data2 = response.json()
print(data2["stats"][5]["base_stat"])
eevee_speed = data2["stats"][5]["base_stat"]

if pika_speed < eevee_speed:
  print("Eevee is faster than Pikachu.")
elif pika_speed > eevee_speed:
  print("Pikachu is faster than Eevee.")
else:
  print("Eevee y Pikachu has the same speed.")
print ("")