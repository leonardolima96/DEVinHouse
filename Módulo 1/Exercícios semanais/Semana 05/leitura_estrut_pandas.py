import pandas as pd


prod = pd.read_csv('produtos.csv')
ped = pd.read_csv('pedidos.csv')
cli = pd.read_csv('clientes.csv')


print('\n', prod)
print(prod.shape)
print('\n', ped)
print(ped.shape)
print('\n', cli)
print(cli.shape)
