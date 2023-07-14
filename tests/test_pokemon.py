import requests
import pytest

token = "50dc7cd67d607596536545fcee858a67"
base_url = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(f'{base_url}/trainers')
    assert response.status_code == 200

def test_name_trainer():
    response = requests.get(f'{base_url}/trainers', params = {"trainer_id": 1372})
    response_body = response.text
    assert response.json()['trainer_name'] == "fitolampa"