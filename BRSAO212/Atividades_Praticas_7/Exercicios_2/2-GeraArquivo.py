#2 - Crie um programa que cria um arquivo  com nome, idade e cidade de algumas pessoas, que este programa escreva os dados em formato tabular e salva no arquivo escolhido pelo usuário, caso ocorra um erro ao salvar, mostre uma mensagem de falha. 

import pandas as pd

try:
    df = pd.DataFrame({
        "Nome": ["João", "Maria", "Pedro", "Ana", "Carlos"],
        "Idade": [25, 30, 35, 40, 45],
        "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador", "Fortaleza"]
    })

    import os
    output_path = os.path.join(os.path.dirname(__file__), "pessoas.csv")
    df.to_csv(output_path, index=False)
    print("Arquivo salvo com sucesso!")
except Exception as e:
    print(f"Erro ao salvar o arquivo: {e}")
