import requests

url = "https://pokeapi.co/api/v2/generation/"
num_generation = str(input("\nIngrese la generación: "))
response = requests.get(url+num_generation).json()
#print(response)


for i in response['pokemon_species']:
    print(i['name'])
    #print(type(i['name']['url']))

