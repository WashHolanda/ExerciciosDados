import pandas as pd
import requests as rq
import json

lst_pokemons = [] #Criação da lista que armazenará os dados dos pokemons e será usada para criação do DataFrame.

#Percorrimento da lista de 150 pokemons da 1 geração com o uso da API.
for i in range(150):
    lst_abilities = [] #Criação da lista auxiliar que armazenará todas as habilidades de determinado pokemon.
    lst_locations = [] #Criação da lista auxiliar que armazenará todos os locais onde determinado pokemon pode ser encontrado.
    
    #Requisição e armazenamento dos dados json vindos da API de cada pokemon (nomes e locais)
    pokemon = rq.get(f"https://pokeapi.co/api/v2/pokemon/{i+1}/")
    pokemon = pokemon.json()
    pokemon_location = rq.get(f"https://pokeapi.co/api/v2/pokemon/{i+1}/encounters")
    pokemon_location = pokemon_location.json()
    #Armazenamento dos dados de habilidades de cada pokemon na lista auxiliar.
    for j, abilities in enumerate(pokemon['abilities']):
        lst_abilities.append(pokemon['abilities'][j]['ability']['name'])
    #Armazenamento dos dados de localização de cada pokemon na lista auxiliar.
    for k, locations in enumerate(pokemon_location):
        lst_locations.append(pokemon_location[k]['location_area']['name'])
    #Armazenamento de todos os dados necessários para criar o DataFrame na lista.
    lst_pokemons.append([pokemon['name'], lst_abilities, lst_locations])

#Criação do DataFrame com todos os dados coletados
df = pd.DataFrame(lst_pokemons, columns=['Nome', 'Lista de Habilidades', 'Área de localização do Pokémon'])

print(df)

'''
Uma forma mais otimizada de requisitar todos os dados da API seria utilizar o conceito de multi-threads no
algoritmo apresentado. Dessa forma, cada thread executaria um laço do for de maneira concorrente, executando
mais de uma requisição ao mesmo tempo e otimizando a montagem do DataFrame.
'''