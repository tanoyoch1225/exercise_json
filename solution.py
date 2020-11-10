from typing import List

# Put your solution in the solution()-function

import json

def solution() -> List[str]:

    # File load
    json_file = open("pokemon_data.json", "r", encoding="UTF-8")
    pokemonLists = json.load(json_file)
    json_file.close

    List = []

    # Extract condiion 1,2,3
    for pokemon in pokemonLists:
        if ('くさ' in pokemon["types"]) \
            and (pokemon["stats"]["hp"] >= 80)\
            and (len(pokemon["abilities"]) + len(pokemon["hiddenAbilities"]) >= 3):
            List.append(pokemon["name"])
    
    # Sort
    List.sort()

    return List