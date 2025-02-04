# Vamos criar uma aplicação com Fast API que retorna nome de cidades de uma país.
# O usuário irá informar o nome do país e a aplicação irá retornar o nome das cidades.
# Utilize o arquivo cities.json para obter os dados.
# O usuário deverá informar o nome do país na URL da aplicação.
# Exemplo: http://

from fastapi import FastAPI
import json

app = FastAPI()

with open('cities.json', 'r') as file:
    data = json.load(file)

@app.get('/{country}')
def get_cities(country: str):
    cities = []
    for city in data:
        if city['country'] == country:
            cities.append(city['name'])
    return {'cities': cities}

# Para rodar a aplicação, execute o comando:
# uvicorn main:app --reload
# Acesse a URL: http://
# Exemplo: http://