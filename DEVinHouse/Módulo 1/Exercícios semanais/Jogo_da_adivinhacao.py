import random


menu = """


        Vamos jogar um jogo?
        
        [1] - Sim
        [2] - Não
        
        """


menu2 = """

    - REGRAS -
    Vou escolher um número de 1 a 100 e você deve adivinhá-lo.
    
    Apenas informarei se o número que você digitou é maior ou menor ao número que escolhi.
    
    Boa sorte. """

while True:
    opcao = input(menu)

    if opcao == "1":
        numero = random.randint(1,100)

        print(menu2)
        
        user_num = int(input("Que número eu escolhi?\n\n"))

        while user_num != numero:
            if user_num > numero:
                user_num = int(input("Você está acima do que eu escolhi, digite um novo número: "))

            elif user_num < numero:
                user_num = int(input("Você está abaixo do número que escolhi, digite um novo número: "))

            elif user_num == numero:
                print("Parabéns, você acertou!")
                
            

    elif opcao == "2":
        break

    else:
        print("Opção inválida, tente novamente")






