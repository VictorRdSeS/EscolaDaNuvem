#4- Verificador de Ano Bissexto

#Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
#Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
year = int(input("Insira um ano para verificar se é bissexto: "))
if is_leap_year(year):
    print("{} é um ano bissexto.".format(year))
else:
    print("{} não é um ano bissexto.".format(year))
