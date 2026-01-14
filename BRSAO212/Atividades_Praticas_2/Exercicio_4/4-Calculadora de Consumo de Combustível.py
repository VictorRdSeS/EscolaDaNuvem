# 4- Calculadora de Consumo de Combustível
# Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

# Distância percorrida: 300 km
# Combustível gasto: 25 litros
# O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.

Distancia_Percorrida = 300  # em km
Combustivel_Gasto = 25      # em litros
Consumo_Medio = Distancia_Percorrida / Combustivel_Gasto
print("Distância Percorrida: {} km".format(Distancia_Percorrida))
print("Combustível Gasto: {} litros".format(Combustivel_Gasto))
print("Consumo Médio: {:.2f} km/l".format(Consumo_Medio))
