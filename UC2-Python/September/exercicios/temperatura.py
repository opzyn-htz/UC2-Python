temperaturas = []
for i in range(7):
    dia = i + 1
    temperaturas.append(float(input(f"Adicione a Temperatura do Dia {dia} --> ")))


media_temp = sum(temperaturas) / len(temperaturas)
acima_media = [temp for temp in temperaturas if temp > media_temp]
duas_ultimas = temperaturas[:-3:-1]
    
print(temperaturas)

print(f"Essa é a soma das temperaturas: {sum(temperaturas)}")
print(f"Essa é a temperatura máxima: {max(temperaturas)}")
print(f"Essa é a temperatura mínima: {min(temperaturas)}")
print(f"Essa é a media das temperaturas: {media_temp}")
print(f"Tivemos somente {len(acima_media)} Temperaturas Acima da Média")
print(f"A lista da maior para menor temperatura: {sorted(temperaturas)}")
print(f"As 2 Últimas Temperaturas são: {duas_ultimas}")

# 1° Exercício pronto