import requests

pokeapi_url = "https://pokeapi.co/api/v2/generation/"
num_generation = str(input("\nIngrese la generación: "))


def api_get_request_generation(num_generation):
    return requests.get(pokeapi_url+num_generation).json()

def get_generation_from_response(response):
    for i in response['pokemon_species']:
        print(f"Nombre: " + i['name'])

def get_info_from_generation(num_generation):
    response = api_get_request_generation(num_generation)
    print(f"\nGeneración {num_generation}:")
    get_generation_from_response(response)
    
get_info_from_generation (num_generation)