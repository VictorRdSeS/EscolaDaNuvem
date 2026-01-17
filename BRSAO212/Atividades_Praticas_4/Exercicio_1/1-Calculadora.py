#1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).

def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero não é permitida."
    return x / y

print("Selecione a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
while True:
    escolha = input("Digite a opção (1/2/3/4) ou 'sair' para encerrar: ")

    if escolha.lower() == 'sair':
        print("Encerrando a calculadora. Até mais!")
        break

    if escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"{num1} + {num2} = {adicionar(num1, num2)}")

        elif escolha == '2':
            print(f"{num1} - {num2} = {subtrair(num1, num2)}")

        elif escolha == '3':
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")

        elif escolha == '4':
            resultado = dividir(num1, num2)
            print(f"{num1} / {num2} = {resultado}")

    else:
        print("Opção inválida. Por favor, tente novamente.")

        