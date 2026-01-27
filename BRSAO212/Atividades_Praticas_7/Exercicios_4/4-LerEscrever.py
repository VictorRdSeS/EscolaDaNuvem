#4 - Crie um programa que leia e escreva arquivos no formato , que salve em um dicionário com nome, idade e cidade em um arquivo JSON e depois leia o mesmo arquivo exibindo os dados, caso o arquivo não existir ou ocorrer erro ao salvar, mostre uma mensagem de falha. 

import json
import os

def main():
    # Dados para salvar
    pessoas = [
        {"nome": "João", "idade": 25, "cidade": "São Paulo"},
        {"nome": "Maria", "idade": 30, "cidade": "Rio de Janeiro"},
        {"nome": "Pedro", "idade": 35, "cidade": "Belo Horizonte"}
    ]

    # Caminho do arquivo no mesmo diretório do script
    nome_arquivo = "dados_pessoas.json"
    caminho_arquivo = os.path.join(os.path.dirname(__file__), nome_arquivo)

    # Escrita do arquivo
    try:
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(pessoas, arquivo, ensure_ascii=False, indent=4)
        print(f"Dados salvos com sucesso em '{nome_arquivo}'.")
    except Exception as e:
        print(f"Falha ao salvar o arquivo: {e}")
        return # Encerra se não conseguiu salvar

    print("-" * 30)

    # Leitura do arquivo
    try:
        if os.path.exists(caminho_arquivo):
            with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
                dados_lidos = json.load(arquivo)
            
            print("Dados lidos do arquivo JSON:")
            for pessoa in dados_lidos:
                print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Cidade: {pessoa['cidade']}")
        else:
            print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

if __name__ == "__main__":
    main()
