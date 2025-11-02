import pandas as pd

data = {'Nome': ['Ana', 'Léo', 'Tati'],
        'Idade': [28,29,28],
        'Cidade': ['Ilhéus', 'Itabuna', 'Salvador']}

df = pd.DataFrame(data)


print(df.describe())


# print(df_info)