# 2 -   Crie um programa que  acesse a API  para buscar um usuário fictício aleatório. exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha.

import requests

url = "https://randomuser.me/api/"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print("Nome: {} {}".format(data["results"][0]["name"]["first"], data["results"][0]["name"]["last"]))
    print("Email: {}".format(data["results"][0]["email"]))
    print("País: {}".format(data["results"][0]["location"]["country"]))
except requests.exceptions.RequestException as e:
    print("Erro na conexão: {}".format(e))
