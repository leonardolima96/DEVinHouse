import csv

with open("vendas.csv", "r", encoding = "utf-8") as vendas:
    leitor = csv.reader(vendas)
    linhas = list(leitor)

    linhas[0].append("total")
    for linha in linhas[1:]:
        quantidade = float(linha[2])
        preco = float(linha[3])

        total = quantidade * preco
        linha.append(f"{total:.2f}")



    with open("vendas.csv", "w", encoding = "utf-8", newline = "") as vendas_new:
        escritor = csv.writer(vendas_new)
        escritor.writerows(linhas)


