produto = {
    "nome": "chevrolet onix",
    "preco": 10000,
    "quantia": 5
}
desconto = float(input("Digite o desconto que queira aplicar, caso NÃO queira aplicar desconto, digite 0 \n>>>"))

produto["preco"]
if desconto >0:
    produto["novo_preco"] = produto['preco'] - (produto["preco"] * desconto / 100) # Define o novo preço do produto com o desconto desejado pelo usuário


print("Desconto não aplicado \n")


print("Valores no dict produto >>>\n")
for c, v in produto.items(): 
    print(c, v) # Printa os pares de chaves que tem no dict


if desconto > 0: print(produto.get('novo_preco'))


if produto["quantia"] < 5:
    print(f"Alerta estoque menor que 5 para >>> {produto['nome']}")

print(produto.get('idade')) # Retorna um valor vazio pois NÃO existe ele no dict!!!

#Atividade Completa