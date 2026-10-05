# Exercício 12 -> O frete da loja virtual

"""
Exercício 12. O frete da loja virtual
    O frete parte de uma faixa de peso: até 2 kg custa R$ 12,00; acima de 2 até 10 kg custa R$ 20,00; acima de
10 kg custa R$ 35,00. Se a distância passar de 100 km, soma-se R$ 0,15 por quilômetro excedente. O frete é
gratuito para compras de R$ 300,00 ou mais, desde que o pacote tenha até 10 kg.
    ▸ O programa recebe o peso, a distância e o valor da compra, e mostra o valor do frete.
    ▸ Quando o frete for gratuito, informe também quanto o cliente teria pago.
    ▸ Testes: 8 kg, 250 km, compra de R$ 180,00; 8 kg, 250 km, compra de R$ 350,00; 12 kg, 350 km, compra
de R$ 400,00.

"""

valor_compra = float(input("Valor da compra: "))
peso = float(input("Peso: "))
distancia = float(input("Distância: "))

# Define o frete pelo peso
if peso <= 2:
    valor_frete = 12
elif peso <= 10:
    valor_frete = 20
else:
    valor_frete = 35

# Adiciona o valor por km excedente
if distancia > 100:
    valor_frete += (distancia - 100) * 0.15

# Verifica se o frete é grátis
if valor_compra >= 300 and peso <= 10:
    valor_frete_pago = valor_frete
    valor_frete = 0

    print("Frete grátis!")
    print(f"Você teria pago R$ {valor_frete_pago:.2f} de frete.")
else:
    print(f"Valor do frete: R$ {valor_frete:.2f}")
