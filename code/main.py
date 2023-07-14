import requests

token = "50dc7cd67d607596536545fcee858a67"
base_url = 'https://api.pokemonbattle.me:9104'

response_add_pokemon = requests.post(f'{base_url}/pokemons', headers={'trainer_token': token}, json={
    "name": "PyPokemon",
    "photo": "https://dolnikov.ru/pokemons/albums/009.png"
})

print(response_add_pokemon.text)

response_rename_pokemon = requests.put(f'{base_url}/pokemons', headers={'trainer_token': token}, json={
    "pokemon_id": "2306",
    "name": "PyTestPokemon2 New",
    "photo": "https://dolnikov.ru/pokemons/albums/009.png"
})

print(response_rename_pokemon.text)

response_add_pokemon_in_pokeball = requests.post(f'{base_url}/trainers/add_pokeball', headers={'trainer_token': token}, json={
    "pokemon_id": "2306"
})

print(response_add_pokemon_in_pokeball.text)