import time

NameDB = ["Opzyn", "Karl", "Abrakadabra"]
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]


class Base:
    def __init__(self, nome, Start: str, Middle_Class: str, End_Class: str):
        self.nome = nome
        self.Start = Start
        self.Middle_class = Middle_Class
        self.End_Class = End_Class

class Start(Base):
    def __init__(self, nome="Sistema", Start: int):
        super().__init__(nome, Start, Midde_Class, End_Class)
        self.soninho = 0.5
        self.second_start = Middle_Class

    def New(self, variable):
        if self.nome == variable:
            print("Abrakadabra")

    def procurar_usuario(self):
        while True:
            nome = input("Qual seu nome? ").strip()

            if nome in NameDB:
                return nome

            print("\nNome não encontrado no sistema.")
            
            for numero in numeros:
                print(f"Numero: {numero}")

            for exu in range(1, 6):
                print(f"\nProcurando no Sistema. Tentativa {exu}/5")
                time.sleep(self.soninho)

            print("\nErro na Busca, code: 404.NotFoundInDB")
            print("Tentando Novamente...\n")

    def iniciar_timer(self):
        print("\nBem Vindo!")

        # Timer de 10 segundos para teste.
        for timer in range(10):
            print(f"System.Load(Timer:{timer} Segundos)")
            time.sleep(1)

        print(f"Você tem muito tempo livre, {self.usuario}!")

    def redo(self, name, naome):
        name = "Abrakadabra"

        if self.nome == naome:
            return name

        return f"Fake chat {self.nome} KKKKKKKKKKK!"

    def executar(self):
        self.usuario = self.procurar_usuario()

        print(f"\nUsuário encontrado: {self.usuario}")

        if self.usuario == "Abrakadabra":
            self.New("Abrakadabra")

        self.iniciar_timer()




class Middle(Start):
    def __init__(self, hora,show,sabimento,probabil):
        self.hora = hora
        self.show = show
        self.sabimento = sabimento
        self.probabil = probabil
        super().__init__(self.second_start)

    def outrage():
        print("Bao")

# Inicia o sistema
sistema = Start()
#sistema.executar() #Variavel que inicia o Start()
meio = Middle()
meio.outrage()
