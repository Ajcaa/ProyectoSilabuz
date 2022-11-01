import requests

pokeapi_generation = "https://pokeapi.co/api/v2/generation/"
pokeapi_pokemon= "https://pokeapi.co/api/v2/pokemon/"
num_generation = str(input("\nIngrese la generación: "))


def api_get_request_generation(num_generation):
    return requests.get(pokeapi_generation+num_generation).json()

def api_get_request_pokemon(name_pokemon):
    return requests.get(pokeapi_pokemon+name_pokemon).json()

def get_generation_from_response(response_generation):
    for i in response_generation['pokemon_species']:
        print(f"\nNombre: " + i['name'])
        get_abilities_from_response(api_get_request_pokemon(i['name']))
        get_image_from_response(api_get_request_pokemon(i['name']))
        
def get_abilities_from_response(response_pokemon):
    for i in response_pokemon['abilities']:
        print("Habilidad:" + i['ability']['name'])    
        
def get_image_from_response(response_pokemon):
    print(response_pokemon['sprites']["front_default"])


def get_info_from_generation(num_generation):
    response_generation = api_get_request_generation(num_generation)
    print(f"\nGeneración {num_generation}:")
    get_generation_from_response(response_generation)
    
    
get_info_from_generation (num_generation)