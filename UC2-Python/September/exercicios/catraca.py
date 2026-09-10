list_users_authorized = ["João", "Marcos", "Carlos Alberto"]

matricula = input("Salve meu cria! Já se matriculou no site? ")

hora = int(input("Que horas são? "))

nome_user = input("Salve cara, aí sim! Poderia me dizer o seu nome para eu conferir aqui? ")

if matricula.lower() == "sim" and nome_user in list_users_authorized and hora < 18:
    print("Bem-vindo ao evento! Catraca liberada.")

elif matricula.lower() != "sim":
    print("Catraca bloqueada: matrícula não está ativa.")

elif nome_user not in list_users_authorized:
    print("Catraca bloqueada: você não está na lista de pessoas autorizadas.")

else:
    print("Catraca bloqueada: o horário já passou das 18h.")