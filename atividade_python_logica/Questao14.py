print("~ ATIVIDADE DE PYTHON ~ ")
print("======================= \n")

# kg >50  = +R$4.00 p/kg
kgLimite = 50

peso = float(input("Informe o peso do peixe em kg: "))

excesso = peso - kgLimite
print("excesso: ",excesso, "Kg")
multa =  bool (excesso>=1) * excesso *4.00

print("Multda pelo Kg excedente: R$", multa)

totalaPagar = peso + multa
print("Total da compra: R$", totalaPagar)
