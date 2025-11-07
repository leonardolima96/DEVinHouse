menu = """


        [1] -- DIGITAR ALGO
        [2] -- SAIR

        """


while True:
    opcao = input(menu).strip()

    if opcao == "1":
        valor = input("Digite algo: ")

        try:
           inteiro = int(valor)
           print("Tipo: inteiro")

        except ValueError:
            try:
               decimal = float(valor)
               print("Tipo: decimal (float)")

            except ValueError:
                print("Tipo: string")

                


    elif opcao == "2":
        print("Saindo...")
        break


    else:
        print("Opção inválida, tente novamente!")


        