compras_joao = ["arroz", "leite", "ovos", "aveia", "chocolate", "carne", "frango"]

compras_maria = ["frango", "sabão", "chá", "chocolate", "ovos", "frutas"]


joao = set(compras_joao)

maria = set(compras_maria)


comuns = joao.intersection(maria)

exclusivos = joao.symmetric_difference(maria)


todos_itens = joao.union(maria)


print("Itens em comum: ", comuns)

print("Itens exclusivos: ", exclusivos)

print("Todos os itens, sem duplicatas: ", todos_itens)