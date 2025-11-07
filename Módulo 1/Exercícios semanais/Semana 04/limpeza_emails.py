import re

emails = ["ana.carla@hotmail.com", "leonardo.lima@gmail.com", "iuri.moraes_@@excel", "lucas____carneiro@@yahoo.com.com.com"]


padrao_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"



validos = []
invalidos = []

for email in emails:
    if re.match(padrao_email, email):
        validos.append(email)
    else:
        invalidos.append(email)


with open("emails_validos.txt", "w", encoding="utf-8") as email_val:
    email_val.write("\n".join(validos))


with open("emails_inválidos.txt", "w", encoding="utf-8") as email_inv:
    email_inv.write("\n".join(invalidos))



print(f"Válidos: \n{validos}")
print(f"Inválidos: \n{invalidos}")

