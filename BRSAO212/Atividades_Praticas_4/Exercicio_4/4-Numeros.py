#4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.

def classificar_numeros(numeros):
    pares = 0
    impares = 0
    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

numeros_usuario = []

while True:
    entrada = input("Digite um número (ou 'sair' para encerrar): ")
    if entrada.lower() == 'sair':
        break
    try:
        numero = int(entrada)
        numeros_usuario.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro ou 'sair'.")

pares, impares = classificar_numeros(numeros_usuario)

print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
