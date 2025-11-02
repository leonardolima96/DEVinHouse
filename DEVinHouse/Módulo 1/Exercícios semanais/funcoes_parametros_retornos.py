# Função para criar uma lista de números
def criar_lista():
    lista = []
    qtd = int(input("Quantos números deseja inserir? "))

    for i in range(qtd):
        while True:
            try:
                num = float(input(f"Digite o {i+1}º número: "))
                lista.append(num)
                break
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
    
    return lista


# Função para calcular a média
def calc_media(numeros):
    media = sum(numeros) / len(numeros)
    return media


# Função para encontrar o maior e o menor valor
def max_min(numeros):
    return max(numeros), min(numeros)


# Função principal (main)
def main():
    print("\n=== CÁLCULO DE MÉDIA, MAIOR E MENOR ===\n")

    numeros = criar_lista()  # cria a lista
    media = calc_media(numeros)  # calcula a média
    maior, menor = max_min(numeros)  # pega o maior e o menor

    # Exibe os resultados formatados
    print("\nRESULTADOS:")
    print(f"Números digitados: {numeros}")
    print(f"Média: {media:.2f}")
    print(f"Maior valor: {maior}")
    print(f"Menor valor: {menor}")


# Execução direta
if __name__ == "__main__":
    main()
