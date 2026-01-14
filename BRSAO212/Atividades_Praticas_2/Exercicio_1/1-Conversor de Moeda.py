# 1- Conversor de Moeda
# Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

# Valor em reais: R$ 100.00
# Taxa do dólar: R$ 5.20
# Taxa do euro: R$ 6.15
# O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

Valor = 100.00
Taxa_Dolar = 5.20
Taxa_Euro = 6.15
Valor_em_Dolar = Valor / Taxa_Dolar
Valor_em_Euro = Valor / Taxa_Euro
print("Valor em Reais: R$ {:.2f}".format(Valor))
print("Valor em Dólares: $ {:.2f}".format(Valor_em_Dolar))
print("Valor em Euros: € {:.2f}".format(Valor_em_Euro))