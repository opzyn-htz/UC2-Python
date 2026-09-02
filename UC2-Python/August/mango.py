import time


nome = input("Olá, qual seu nome? Poderia informá-lo aqui: ")

compra = input(
    f"\nBem-vindo à Cantina, {nome}!\n"
    "O que desejas comprar?\n"
    "1 - Manga -------- R$ 12.50\n"
    "2 - Leite -------- R$ 6.50\n"
    "3 - Manga com leite R$ 18.00\n"
    "0 - Sair\n"
    "Digite sua escolha: "
)


while compra != "0":

    match compra:

        #Processo da Manga
        case "1":
            mango = 12.50

            decision = input(
                "\nVocê gostaria de comprar mais de uma manga? "
            )
            #Transforma em caixa baixa para ler as condições, ex: Usuário digita SiM, o .lower() transforma em: sim
            if decision.lower() not in ("nao", "não"):

                print(
                    "\nPerfeito! Apenas nos informe "
                    "quantas mangas gostaria de comprar!"
                )

                mango_qnt = int(
                    input("Gostaria de comprar quantas mangas? ")
                )

            else:
                mango_qnt = 1

            new_mango = mango * mango_qnt

            pagar = input(
                f"\nO valor final seria R$ {new_mango:.2f}. "
                "Gostaria de prosseguir com o pagamento? "
            )

            if pagar.lower() not in ("nao", "não"):

                print("\nPagamento iniciado!")
                time.sleep(1)

                print("Pagamento em processo...")
                time.sleep(3)

                print(
                    "Pagamento concluído! "
                    "Aproveite o seu lanche!"
                )

            else:
                print("\nCompra cancelada.")

            break


        #Processo do Leite
        case "2":
            leite = 6.50

            decision = input(
                "\nVocê gostaria de comprar mais de um leite? "
            )

            if decision.lower() not in ("nao", "não"):

                leite_qnt = int(
                    input("Gostaria de comprar quantos leites? ")
                )

            else:
                leite_qnt = 1

            new_leite = leite * leite_qnt

            pagar = input(
                f"\nO valor final seria R$ {new_leite:.2f}. "
                "Gostaria de prosseguir com o pagamento? "
            )

            if pagar.lower() not in ("nao", "não"):
                #Pagamento em ação, aguarda 1 seg para prosseguir
                print("\nPagamento iniciado!")
                time.sleep(1)
                #Pagamento em ação, aguarda 3 seg para prosseguir
                print("Pagamento em processo...")
                time.sleep(3)

                print(
                    "Pagamento concluído! "
                    "Aproveite o seu lanche!"
                )

            else:
                print("\nCompra cancelada.")

            break


        #Processo da Manga com Leite
        case "3":
            manga_leite = 18.00

            decision = input(
                "\nVocê gostaria de comprar mais de uma porção? "
            )

            if decision.lower() not in ("nao", "não"):

                porcao_qnt = int(
                    input("Gostaria de comprar quantas porções? ")
                )

            else:
                porcao_qnt = 1

            new_manga_leite = manga_leite * porcao_qnt

            pagar = input(
                f"\nO valor final seria R$ {new_manga_leite:.2f}. "
                "Gostaria de prosseguir com o pagamento? "
            )

            if pagar.lower() not in ("nao", "não"):

                print("\nPagamento iniciado!")
                time.sleep(1)

                print("Pagamento em processo...")
                time.sleep(3)

                print(
                    "Pagamento concluído! "
                    "Aproveite o seu lanche!"
                )

            else:
                print("\nCompra cancelada.")

            break

        # Deu erro né
        case _:
            print(
                "\nOpção inválida! "
                "Por favor, escolha 1, 2, 3 ou 0 -> Sair da Aplicação."
            )

            compra = input(
                "\nDigite sua escolha novamente: "
            )


print(f"\nObrigado pela preferência, {nome}!")
print("Volte sempre à Cantina!")