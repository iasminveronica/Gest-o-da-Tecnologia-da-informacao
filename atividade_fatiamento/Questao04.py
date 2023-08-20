print("QUESTÃO 5: Verificação de acesso")

nome = input("Informe seu nome: ") # Iasmin Veronica
idade = int(input("Informe sua idade: "))
sexo = input("Informe seu sexo: ").upper()
posi = nome.find(" ")  # 6
if sexo[0] == "F" and idade <= 25:
    print(nome[:posi].upper(),"= ACEITA") # nome[0:6]
else:
    print("NÃO ACEITA!")

print("\n\n\n\n--------------------------")
print("FIM DA QUESTÃO")