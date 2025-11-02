menu = """


        DIGITE A OPÇÃO DESEJADA
        
            [1] -- Converter unidades
            [2] -- Sair
            
            
            """



tcel = 0
tfah = 0
tkel = 0
tcel_tfah = 0
tcel_tkel = 0
tfah_tcel = 0
tfah_tkel = 0
tkel_tcel = 0
tkel_tfah = 0


while True:
    opcao = input(menu)

    if opcao == "1":

        menu2 = """

        Digite o tipo de conversão que quer fazer
        
            [1] -- Celsius para Fahrenheit
            [2] -- Fahrenheit para Celsius
            [3] -- Celsius para Kelvin
            [4] -- Kelvin para Celsius
            [5] -- Fahrenheit para Kelvin
            [6] -- Kelvin para Fahrenheit
            [7] -- Sair
            
            """
        
        opcao2 = input(menu2)

        if opcao2 == "1":
            tcel = float(input("Digite a temperatura (°C): "))
            
            tcel_tfah = (tcel * 9/5) + 32

            print(f"Resultado: {tcel_tfah:.2f}°F\n")


        elif opcao2 == "2":
            tfah = float(input("Digite a temperatura (°F): "))
                        
            tfah_tcel = (5*(tfah - 32))/9

            print(f"Resultado: {tfah_tcel:.2f}°C")

        elif opcao2 == "3":
             tcel = float(input("Digite a temperatura (°C): "))

             tcel_tkel = tcel + 273.15
             print(f"Resultado: {tcel_tkel:.2f}K\n")

        elif opcao2 =="4":
            tkel = float(input("Digite a temperatura (K): "))

            tkel_tcel = tkel - 273.15

            print(f"Resultado: {tkel_tcel:.2f}°C\n")

        elif opcao2 =="5":
            tfah = float(input("Digite a temperatura (°F): "))

            tfah_tkel = (5*(tfah - 32))/9 + 273.15

            print(f"Resultado: {tfah_tkel:.2f}K\n")

        elif opcao2 =="6":
            tkel = float(input("Digite a temperatura (K): "))

            tkel_tfah = ((tkel - 273.15)*9/5) + 32

            print(f"Resultado: {tkel_tfah:.2f}°F\n")


        elif opcao2 == "7":
            break


    elif opcao == "2":
        break



    else:
        print("Opção inválida, por favor tente novamente!")
