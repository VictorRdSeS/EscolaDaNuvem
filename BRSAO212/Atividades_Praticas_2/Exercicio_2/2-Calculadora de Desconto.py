# 2- Calculadora de Desconto
# Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

# Nome do produto: "Camiseta"
# Preço original: R$ 50.00
# Porcentagem de desconto: 20%
# O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

Nome_Produto = "Camiseta"
Preco_Original = 50.00
Porcentagem_Desconto = 20
Valor_Desconto = (Porcentagem_Desconto / 100) * Preco_Original
Preco_Final = Preco_Original - Valor_Desconto
print("Produto: {}".format(Nome_Produto))
print("Preço Original: R$ {:.2f}".format(Preco_Original))
print("Porcentagem de Desconto: {}%".format(Porcentagem_Desconto))
print("Valor do Desconto: R$ {:.2f}".format(Valor_Desconto))
print("Preço Final: R$ {:.2f}".format(Preco_Final))


