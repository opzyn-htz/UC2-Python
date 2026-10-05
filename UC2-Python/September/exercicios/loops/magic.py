
#2 loops que fazem a mesma coisa, mas 1 com while e outro com for
numero = 1
while numero !=11:
    print(numero)
    numero+=1

#print("mango")

for i in range(1, 11):
    print(i)

#mangic

# Numero que diz a tabuada de 1 a 10

p_num = int(input("Primeiro número: "))
tab_atual = 1
while tab_atual !=11:
    print(p_num * tab_atual)
    tab_atual+=1

# Código que printa cada um do caracter da str e identifica se tem vogais

conjunto = "mango arabico abc1234456667758865685785687".lower()
vogais = 0
for i in conjunto:
    print(i)
    if i in ['a', 'e', 'i', 'o', 'u']:
        vogais +=1

print(f"A string conjunto tem {len(conjunto)} caracteres e {vogais} vogais")

# Eu duvido da minha lógica, mas da certo

p_num = int(input("Primeiro número: "))
tab_atual = 1
while p_num <=101:
    print(f"Tabuada : {p_num} x {tab_atual} = {p_num * tab_atual}")
    tab_atual+=1
    if tab_atual ==11:
        p_num +=1
    if p_num == 101:
        break

    if tab_atual >=11:
        tab_atual = 1
