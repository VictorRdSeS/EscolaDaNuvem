# 4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.

import datetime
    
def dias_vivo(data_nascimento_str):
    try:
        data_nascimento = datetime.datetime.strptime(data_nascimento_str, "%d/%m/%Y").date()
        data_atual = datetime.date.today()
        return (data_atual - data_nascimento).days
    except ValueError:
        return None

data_nascimento_input = input("Digite sua data de nascimento (DD/MM/AAAA): ")
dias = dias_vivo(data_nascimento_input)

if dias is not None:
    print(f"Você está vivo há {dias} dias.")
else:
    print("Formato de data inválido. Use DD/MM/AAAA.")