produtos = {

    "Volante": 250.00,
    "Porta": 120.00,
    "Banco": 55.00,
    "Para-brisa": 87.50,
    "Motor": 654.99,
    "Câmbio": 99.98

    
}
for produto, preco in produtos.items():
    if preco > 100:
        print(produto, preco)