import requests
import json

pokemon_name = (input("Enter Pokemon: ")).lower()


def get_pokemon(pokemon_name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    #print(response.status_code)
    #print(response.text)

    payload = response.text
    json_obj = json.loads(payload)


    abilities = json_obj['abilities']
    i = 0

    for i in abilities:
        print(i)

        

get_pokemon(pokemon_name)