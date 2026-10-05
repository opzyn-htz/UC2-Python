# Exercício -> Temperatura para quem viaja

"""
    Um site de viagens informa a temperatura em três escalas e diz o que esperar do dia. Fahrenheit é a
temperatura em Celsius multiplicada por 9, dividida por 5 e somada a 32. Kelvin é a temperatura em Celsius
somada a 273,15.
    ▸ O programa recebe a temperatura em Celsius e mostra as três escalas.
    ▸ Mostre também a classificação: abaixo de 15 graus é frio, de 15 a 28 é agradável, acima de 28 é
    quente.
    ▸ Testes: 30 graus e 15 graus.

"""

temp_celsius = float(input("Qual a temperatura de hoje?\n>>> ")) # Requisita a temperatura do usuário

calc_fah = temp_celsius * 1.8 + 32 # Converte para Fahrenheit
calc_kelvin = temp_celsius + 273.15 # Converte para Kelvin

if temp_celsius <= 15:
    print("Esta frio hoje")
elif temp_celsius >15 and temp_celsius <= 28:
    print("Hoje o clima ta bom")
else:
    print("Ta quente demais hoje")
print(f" A Temperatura em diferentes medidas são: \nGraus Celsius ->{temp_celsius}\nFahrenheit -> {calc_fah}\n Kelvin -> {calc_kelvin}")
