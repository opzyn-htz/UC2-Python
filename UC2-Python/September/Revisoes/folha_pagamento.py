# Exercício -> A folha de pagamento

'''
    Exercício 11. A folha de pagamento

    A empresa paga por hora. Até 220 horas no mês, a hora vale o valor normal. As horas que passarem de 220
valem 50% a mais. Sobre o salário bruto incide o desconto do INSS: 7,5% para bruto de até R$ 1.500,00; 9%
para bruto acima disso até R$ 2.800,00; e 12% para bruto acima de R$ 2.800,00. Use a alíquota única sobre
o valor total, sem cálculo progressivo.
    ▸ O programa recebe o nome, o valor da hora e as horas trabalhadas no mês.
    ▸ Mostre o salário bruto, o valor do INSS e o salário líquido, todos com duas casas decimais.
    ▸ Testes: R$ 12,00 a hora com 240 horas; depois R$ 12,00 a hora com 200 horas

'''
nome = input("Nome: ")
horas = float(input("Quantas horas foram trabalhadas este mês?\n>>> "))
valor_hora = float(input("Valor da hora: "))

if horas <= 220:
    salario_bruto = horas * valor_hora
else:
    horas_extras = horas - 220
    salario_bruto = (220 * valor_hora) + (horas_extras * valor_hora * 1.5)

if salario_bruto <= 1500:
    inss = salario_bruto * 0.075
elif salario_bruto <= 2800:
    inss = salario_bruto * 0.09
else:
    inss = salario_bruto * 0.12

salario_liquido = salario_bruto - inss

print("Nome:", nome)
print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"INSS: R$ {inss:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")