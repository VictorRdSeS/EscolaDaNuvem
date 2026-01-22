# 3 - Crie um programa que consulte informações de um  na API , retorne logradouro, bairro, cidade e estado do CEP digitado, caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha.

import requests

cep = input("Digite o CEP: ")
url = "https://viacep.com.br/ws/{}".format(cep)+"/json/"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print("Logradouro: {}".format(data["logradouro"]))
    print("Bairro: {}".format(data["bairro"]))
    print("Cidade: {}".format(data["localidade"]))
    print("Estado: {}".format(data["uf"]))
except requests.exceptions.RequestException as e:
    print("Erro na conexão: {}".format(e))
