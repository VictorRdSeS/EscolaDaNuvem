# 2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.

def palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]

# Testando a função
texto = input("Digite uma palavra ou frase: ")
if palindromo(texto):
    print("Sim")
else:
    print("Não")
    