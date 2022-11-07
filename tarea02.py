import requests
from os import system

again = True

pokeapi_generation = "https://pokeapi.co/api/v2/generation/"
pokeapi_pokemon= "https://pokeapi.co/api/v2/pokemon/" 
pokeapi_ability = "https://pokeapi.co/api/v2/ability/"
url_hab = "https://pokeapi.co/api/v2/pokemon-habitat/"
url_type = "https://pokeapi.co/api/v2/type/"

# Funcion Menu
def menu(answerMenu,again):
    system("cls")
    if answerMenu != "y":
        again = False
    return again

# Obtiene el request de Generation
def api_get_request_generation(num_generation):
    return requests.get(pokeapi_generation+num_generation).json()
        
# Obtiene el request de Pokemon
def api_get_request_pokemon(name_pokemon):
    return requests.get(pokeapi_pokemon+name_pokemon).json()

# Obtiene el request de Habilidad
def api_get_request_ability(nom_ability):
    return requests.get(pokeapi_ability+nom_ability).json()      

# Obtiene el request de Habitat
def api_get_request_habitat(nom_hab):
    return requests.get(url_hab + nom_hab).json()  

# Obtiene el request de Types
def api_get_request_type(nom_type):
    return requests.get(url_type+nom_type).json() 


# Obtiene los datos de la generacion del requests   
def get_generation_from_response(response_generation):
    for i in response_generation['pokemon_species']:
        if requests.get(pokeapi_pokemon+i['name']).status_code != 404:
            print(f"\nNombre: ", i['name'].capitalize())
            get_abilities_from_response(api_get_request_pokemon(i['name']))
            get_image_from_response(api_get_request_pokemon(i['name']))
        
# Obtiene los datos de las habilidades del requests         
def get_abilities_from_response(response_pokemon):
    for i in response_pokemon['abilities']:
        print("Habilidad:", i['ability']['name'].capitalize())  
      
# Obtiene los datos de la url-imagen del requests           
def get_image_from_response(response_pokemon):
    print("Imagen:", response_pokemon['sprites']["front_default"])
            
# Obtiene los datos de las habilidades del requests 
def get_ability_from_response(response_ability):
    for i in response_ability['pokemon']:
        print(f"\nNombre: ", i['pokemon']['name'].capitalize())
        get_abilities_from_response(api_get_request_pokemon(i['pokemon']['name']))
        get_image_from_response(api_get_request_pokemon(i['pokemon']['name'])) 

# Obtiene los datos del habitat del requests 
def habitat_from_rp(response_habitat):
    for i in response_habitat['pokemon_species']:
        print(f"\nNombre: ", i['name'].capitalize())
        get_abilities_from_response(api_get_request_pokemon(i['name']))
        get_image_from_response(api_get_request_pokemon(i['name'])) 
        
# Obtiene los datos de los tipos del requests         
def types(tipo_response):
    for i in tipo_response['pokemon']:
        print("\nNombre: ",i['pokemon']['name'].capitalize())
        get_abilities_from_response(api_get_request_pokemon(i['pokemon']['name']))
        get_image_from_response(api_get_request_pokemon(i['pokemon']['name']))

# Obtiene los datos de las formas del requests    
def get_form_from_response(response_form):
    for i in response_form['forms']:
        print("Forma: ",i['name'].capitalize())
    get_abilities_from_response(api_get_request_pokemon(response_form['name']))
    get_image_from_response(api_get_request_pokemon(response_form['name'])) 
    

# Obtiene todos los datos finales de generacion  
def get_info_from_generation(num_generation):
    response_generation = api_get_request_generation(num_generation)
    print(f"\nGeneración {num_generation}:")
    get_generation_from_response(response_generation)

# Obtiene todos los datos finales de las habilidades  
def get_info_from_ability(nom_ability):
    response_ability = api_get_request_ability(nom_ability)
    print(f"\nHabilidad: {nom_ability}:")
    get_ability_from_response(response_ability)
    
# Obtiene todos los datos finales del habitat 
def info_habitat(nom_hab):
    response_habitat = api_get_request_habitat(nom_hab) 
    print("\nHabitat:",nom_hab)       
    habitat_from_rp(response_habitat)
    
# Obtiene todos los datos finales de los tipos
def get_info_from_type(nom_type):
    type_response = api_get_request_type(nom_type)
    print("\nTipo:", nom_type)
    types(type_response)
    
# Obtiene todos los datos finales de las formas
def get_info_from_form(num_form):
    response_form = api_get_request_pokemon(num_form)
    print("\nPokemon:",num_form)
    get_form_from_response(response_form)
    

while again == True:

    print('''
                                            POKEAPI
                            Opción 1: Listar pokemons por generación.
                            Opción 2: Listar pokemons por forma. 
                            Opción 3: Listar pokemons por habilidad.
                            Opción 4: Listar pokemons por habitat.
                            Opción 5: Listar pokemons por tipo.
                            Opción 6: Salir.

    ''')


    option = int(input("Elija el numero de una opcion:  "))
    while option not in (1, 2, 3, 4, 5, 6):
        option = int(input("Debe elegir un numero de la opcion (1,2,3,4,5): "))



    if option == 1:

        print("---------------------------*-OPCION 1-----------------------------")
        print("""
                                    GENERACIONES DE POKEMON
                                        1            5         
                                        2            6        
                                        3            7      
                                        4            8
                                                
        """
        )
        
        num_generation = str(input("\nIngrese la generación: "))
        get_info_from_generation (num_generation)
        
        retornMenu = input("\n¿Deseas volver al menu? [y/n]: ").lower()
        again=menu(retornMenu,again)
            
        

    if option == 2:
        print("---------------------------*-OPCION 2-----------------------------")
        print("Ejemplos: \n412 <-> burmy \n421 <-> cherrim \n493 <-> arceus \n716 <-> xerneas")
        
        num_form = str(input("\nIngrese el id o un nombre del pokemon: "))
        get_info_from_form (num_form)
        
        retornMenu = input("\n¿Deseas volver al menu? [y/n]: ").lower()
        again=menu(retornMenu,again)


    if option == 3:

        print("--------------------------------OPCION 3--------------------------------")


        print("""
                                        HABILIDADES DE POKEMON
                1. stench           6. damp           11. water-absorb      16. color-change 
                2. drizzle          7. limber         12. oblivious         17. immunity
                3. speed-boost      8. sand-veil      13. cloud-nine        18. flash-fire
                4. battle-armor     9. static         14. compound-eyes     19. shield-dust
                5. sturdy           10.volt-absorb    15. insomnia          20. own-tempo
        """
        )

        nom_ability = str(input("\nIngrese el ID o nombre de la habilidad: "))
        get_info_from_ability (nom_ability)

        retornMenu = input("\n¿Deseas volver al menu? [y/n]: ").lower()
        again=menu(retornMenu,again)



    if option == 4:

        print("--------------------------------OPCION 4--------------------------------")


        print("""
                                        HABITATS DE POKEMONS

                                    1. Cave         6. Rough-terrain                  
                                    2. Forest       7. Sea                   
                                    3. Grassland    8. Urban             
                                    4. Mountain     9. Waters-edge            
                                    5. Rare                    
        """
        )

        nom_hab = str(input("\nIngrese el id o un nombre de habitat: ")) 
        info_habitat(nom_hab)

        retornMenu = input("\n¿Deseas volver al menu? [y/n]: ").lower()
        again=menu(retornMenu,again)



    if option == 5:
        print("--------------------------OPCION 5--------------------------")

        print("""
                                    TIPOS DE POKEMON
                1. normal      6. rock          11.  water         16. dragon   
                2. fighting    7. bug           12.  grass         17. dark
                3. flying      8. ghost         13.  electric      18. fairy
                4. poison      9. steel         14.  psychic       
                5. ground      10. fire         15.  ice           
        """
        )

        nom_type = str(input("Inserte la ID o nombre de un Tipo de pokemon:  "))
        get_info_from_type(nom_type)

        retornMenu = input("\n¿Deseas volver al menu? [y/n]: ").lower()
        again=menu(retornMenu,again)
        
    if option == 6:
        again = False
        print("El programa a finalizado.") 