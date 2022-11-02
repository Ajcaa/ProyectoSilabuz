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




print("""
                            TIPOS DE POKEMON
        1. normal      6. rock          11.  water         16. dragon   
        2. fighting    7. bug           12.  grass         17. dark
        3. flying      8. ghost         13.  electric      18. fairy
        4. poison      9. steel         14.  psychic       
        5. ground      10. fire         15.  ice           
"""
)


url = "https://pokeapi.co/api/v2/type/"
url_poke= "https://pokeapi.co/api/v2/pokemon/"

elija = str(input("Inserte la ID o nombre de un Tipo de pokemon:  "))



def url_tipo(elija):
    return requests.get(url+elija).json() 
def url_pokemon(pokemon):
    return requests.get(url_poke+pokemon).json() 





def tipos(tipo_response):
    for i in tipo_response['pokemon']:
        print(i['pokemon']['name'])
        habilidades(url_pokemon(i['pokemon']['name']))
        imagen(url_pokemon(i['pokemon']['name']))


def habilidades(poke_response):
    for i in poke_response['abilities']:
        print("Habilidad:", i['ability']['name'])

def imagen(poke_response):  
    print(poke_response['sprites']['front_default'])


def info_general(elija):
    tipo_response = url_tipo(elija)
    print("n/Tipo:", elija)
    tipos(tipo_response)


info_general(elija)

print("Test")