import requests

print('''
                                        POKEAPI
                        Opción 1: Listar pokemons por generación.
                        Opción 2: Listar pokemons por forma. 
                        Opción 3: Listar pokemons por habilidad.
                        Opción 4: Listar pokemons por habitat.
                        Opción 5: Listar pokemons por tipo.

''')

#Agregar Imagenes

option = int(input("Elija el numero de una opcion:  "))

if option == 1:

    print("------------------------------OPCION 1----------------------------")


    print("""
                                GENERACIONES DE POKEMON
                                    1            5         
                                    2            6        
                                    3            7      
                                    4            8
                                               
"""
    )

    

    pokeapi_generation = "https://pokeapi.co/api/v2/generation/"
    pokeapi_pokemon= "https://pokeapi.co/api/v2/pokemon/"  #pokeapi_pokemon
    try: 
        num_generation = str(input("\nIngrese la generación: "))
    except requests.exceptions.JSONDecodeError:
        print("No es un numero valido")
        



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


















if option == 3:

    print("------------------------------OPCION 3----------------------------")


    print("""
                                    HABILIDADES DE POKEMON
            1. stench           6. damp           11. water-absorb      16. color-change 
            2. drizzle          7. limber         12. oblivious         17. immunity
            3. speed-boost      8. sand-veil      13. cloud-nine        18. flash-fire
            4. battle-armor     9. static         14. compound-eyes     19. shield-dust
            5. sturdy           10.volt-absorb    15. insomnia          20. own-tempo
    """
    )



    pokeapi_ability = "https://pokeapi.co/api/v2/ability/"
    pokeapi_poke= "https://pokeapi.co/api/v2/pokemon/"  #pokeapi_poke
    nom_ability = str(input("\nIngrese el ID o nombre de la habilidad: "))


    def request_ability(nom_ability):
        return requests.get(pokeapi_ability+nom_ability).json()

    def request_pokemon(name_poke):
        return requests.get(pokeapi_pokemon+name_poke).json()

    def get_ability_from_rsp(response_ability):
        for i in response_ability['pokemon']:
            print(f"\nNombre: " + i['pokemon']['name'])
            get_abilities_from_rsp(request_pokemon(i['pokemon']['name']))
            get_image_from_rsp(request_pokemon(i['pokemon']['name']))
            
    def get_abilities_from_rsp(rsp_pokemon):
        for i in rsp_pokemon['abilities']:
            print("Habilidad:" + i['ability']['name'])    
            
    def get_image_from_rsp(rsp_pokemon):
        print(rsp_pokemon['sprites']["front_default"])


    def get_info_from_ability(nom_ability):
        response_ability = request_ability(nom_ability)
        print(f"\nHabilidad: {nom_ability}:")
        get_ability_from_rsp(response_ability)
        
        
    get_info_from_ability (nom_ability)





if option == 4:

    print("-----------------------------OPCION 4------------------------------")


    print("""
                                    HABITATS DE POKEMONS

                                1. Cave         6. Rough-terrain                  
                                2. Forest       7. Sea                   
                                3. Grassland    8. Urban             
                                4. Mountain     9. Waters-edge            
                                5. Rare                    
    """
    )


    url_hab = "https://pokeapi.co/api/v2/pokemon-habitat/"
    urlPoke= "https://pokeapi.co/api/v2/pokemon/"  #cambiar nombre a url a urlPoke

    nom_hab = str(input("\nIngrese el id o un nombre de habitat: ")) #agregar ID habitat

    def url_habitat(nom_hab):
        return requests.get(url_hab + nom_hab).json()

    def urlPokemon(namePoke):  #cambiar el nombre de name_pokemon  a   namePoke
        return requests.get(urlPoke+namePoke).json()




    def habitat_from_rp(response_habitat):
        for i in response_habitat['pokemon_species']:
            print(f"\nNombre: " + i['name'])
            abilities_from_rp(urlPokemon(i['name']))
            get_image_from_rp(urlPokemon(i['name']))
            
    def abilities_from_rp(rp_pokemon):
        for i in rp_pokemon['abilities']:
            print("Habilidad:" + i['ability']['name'])    
            
    def get_image_from_rp(rp_pokemon):
        print(rp_pokemon['sprites']["front_default"])


    def info_habitat(nom_hab):
        response_habitat = url_habitat(nom_hab) 
        print("\nHabitat:",nom_hab)       
        habitat_from_rp(response_habitat)
        
        
    info_habitat(nom_hab)




if option == 5:
    print("-----------------------------OPCION 5------------------------------")

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
        print("\nTipo:", elija)
        tipos(tipo_response)


    info_general(elija)
