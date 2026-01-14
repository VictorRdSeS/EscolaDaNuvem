#3- Conversor de Temperatura
#Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
#O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

temperature = float(input("Insira a temperatura a ser convertida: "))
from_unit = input("Insira a unidade de origem (C, F, K): ").upper()
to_unit = input("Insira a unidade para a qual deseja converter (C, F, K): ").upper()

if from_unit == "C":
    if to_unit == "F":
        converted = celsius_to_fahrenheit(temperature)
        print("Temperatura convertida: {:.2f} °F".format(converted))
    elif to_unit == "K":
        converted = celsius_to_kelvin(temperature)
        print("Temperatura convertida: {:.2f} K".format(converted))
    else:
        converted = temperature
        print("Temperatura convertida: {:.2f} °C".format(converted))
elif from_unit == "F":
    if to_unit == "C":
        converted = fahrenheit_to_celsius(temperature)
        print("Temperatura convertida: {:.2f} °C".format(converted))
    elif to_unit == "K":
        converted = fahrenheit_to_kelvin(temperature)
        print("Temperatura convertida: {:.2f} K".format(converted))
    else:
        converted = temperature
        print("Temperatura convertida: {:.2f} °F".format(converted))
elif from_unit == "K":
    if to_unit == "C":
        converted = kelvin_to_celsius(temperature)
        print("Temperatura convertida: {:.2f} °C".format(converted))
    elif to_unit == "F":
        converted = kelvin_to_fahrenheit(temperature)
        print("Temperatura convertida: {:.2f} °F".format(converted))
    else:
        converted = temperature
        print("Temperatura convertida: {:.2f} K".format(converted))
else:
    print("Unidade de origem inválida.")
    exit()