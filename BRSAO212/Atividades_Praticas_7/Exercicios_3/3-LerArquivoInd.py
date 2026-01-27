#3 -  Crie um programa que leia um arquivo  informado pelo usuário, percorrendo cada linha do arquivo e a exibe na tela, caso o arquivo não seja encontrado, mostre uma mensagem de erro.

import pandas as pd

try:
    df = pd.read_csv("pessoas.csv")
    for index, row in df.iterrows():
        print(f"Index: {index}, Nome: {row['Nome']}, Idade: {row['Idade']}, Cidade: {row['Cidade']}")
except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")
