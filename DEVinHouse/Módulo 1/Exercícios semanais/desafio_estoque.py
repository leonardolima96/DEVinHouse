import pandas as pd

df_produtos = pd.read_csv("produtos.csv")

estoque_baixo = df_produtos[df_produtos['estoque']< 20]

estoque_baixo.to_csv("produtos_baixo_estoque.csv", index=False, encoding="utf-8")