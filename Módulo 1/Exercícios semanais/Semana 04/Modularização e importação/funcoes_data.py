import datetime

def dif_fim_ano():

    indata = input("Digite uma data dd/mm/yyyy: ")

    usdata = datetime.datetime.strptime(indata, "%d/%m/%Y",).date()


    fim_ano = datetime.date(usdata.year, 12, 31)

    dias_rest = (fim_ano - usdata).days


    print(f"Faltam {dias_rest:.2f} dias para o fim de {fim_ano.year}")
