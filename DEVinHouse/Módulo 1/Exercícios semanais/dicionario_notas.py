turma_b = {


    'Eduardo':[8, 7.5, 6,],
    'Jessica':[9,10,10,],
    'Monica':[6,4.75,8,],
    'Dorgival':[4,6,6.5,],
}


for nome, nota in turma_b.items():
    media = float(sum(nota)/len(nota))

    if media >= 7:
       print(f"Aprovados: {nome} - {media:.2f}")