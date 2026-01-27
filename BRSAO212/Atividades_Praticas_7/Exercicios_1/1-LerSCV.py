#1 -  Crie um programa que lê um arquivo CSV de  com a biblioteca , calcule e exiba a  e o  da coluna tempo_execucao, caso e o arquivo não exista ou houver erro na leitura, mostre uma mensagem de erro. 

import pandas as pd
import os

# Pega o caminho da pasta onde o script (.py) está salvo
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_csv = os.path.join(diretorio_atual, "arquivo.csv")

try:
    df = pd.read_csv(caminho_csv)
    print(f"Média: {df['tempo_execucao'].mean():.2f}")
    print(f"Mediana: {df['tempo_execucao'].median():.2f}")

except FileNotFoundError:
    print(f"Erro: O arquivo não foi encontrado em: {caminho_csv}")
except Exception as e:
    print(f"Erro inesperado: {e}")
        
