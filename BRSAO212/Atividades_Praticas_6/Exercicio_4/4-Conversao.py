# 4 - Crie um programa que realize consultas a  em relação ao Real (BRL) usando a API mostre valor atual, máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.

import requests

url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print("Valor atual: {}".format(data["USDBRL"]["ask"]))
    print("Máxima: {}".format(data["USDBRL"]["high"]))
    print("Mínima: {}".format(data["USDBRL"]["low"]))
    print("Data/hora da última atualização: {}".format(data["USDBRL"]["create_date"]))
except requests.exceptions.RequestException as e:
    print("Erro na conexão: {}".format(e))
