def num_alunos(prompt):
    while True:
        try:
            v = int(input(prompt))
            if v > 0:
                return v
            print("Informe um número inteiro positivo")

        except ValueError:
            print("Entrada inválida")



def ler_notas(prompt):
    while True:
        try:
            n = float(input(prompt))
            if 0 <= n <= 10:
                return n
            print("A nota deve ser um valor entre 0 e 10")

        except ValueError:
            print("Nota inválida")


def cadastrar_alunos(cadastro):
    qtd = num_alunos("Informe o número de alunos a serem cadastrados: ")
    for i in range(1, qtd+1):
        nome = input(f"Nome do aluno {i}: ").strip()

        while not nome:
            nome = input("Nome inválido. DIgite o nome do aluno: ").strip()



        notas = []
        notas.append(ler_notas("   Informe a 1ª nota   "))
        notas.append(ler_notas("   Informe a 2ª nota   "))
        notas.append(ler_notas("   Informe a 3ª nota   "))

        cadastro[nome] = notas



def imprimir_relacao(cadastro):
    if not cadastro:
        print("Não há registros")
        return
    

    aprovados = {}
    reprovados = {}
    for nome, notas in cadastro.items():
        media = float(sum(notas)/len(notas))
        if media >= 7:
            aprovados[nome] = media

        else:
            reprovados[nome] = media


    print("\nAprovados\n")
    if aprovados:
        for nome, media in aprovados.items():
            print(f"{nome}: média {media:.2f}")

    else:
        print("Nenhum aluno aprovado")

    print("\nReprovados\n")
    if reprovados:
        for nome, media in reprovados.items():
            print(f"{nome}: média {media:.2f}")

    else:
        print("Nenhum aluno reprovado")


    print()

def main():
    cadastro = {}
    menu = """

            BEM VINDO AO SISTEMA DE CADASTRO DE NOTAS
            POR FAVOR, INFORME A OPÇÃO DESEJADA:
            
            [1] -- CADASTRAR ALUNOS
            [2] -- IMPRIMIR RELAÇÃO DE APROVADOS/REPROVADOS
            [3] -- SAIR
            
            
            """
    

    while True:
        opcao = input(menu).strip()

        if opcao == "1":
            cadastrar_alunos(cadastro)
        elif opcao == "2":
            imprimir_relacao(cadastro)
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.\n")


if __name__ == "__main__":
    main()


