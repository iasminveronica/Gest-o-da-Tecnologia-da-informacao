print("QUESTÃO 9:\
Faça um programa que receba do usuário uma string.\
O programa imprime a string sem suas vogais.")

meses = "janeiro" \
         "fevereiro"\
         "março" \
         "abril" \
         "maio" \
         "junho" \
         "julho" \
         "agosto" \
         "setembro" \
         "outubro" \
         "novembro" \
         "dezembro"
data = input("informe sua data de nascimento: ")
print (data.split("/")[0], "de", meses[(int(data.split("/")[1])-1)] , 
        "de", data.split("/")[2]) 

print("\n\n--------------------------")
print("FIM DA QUESTÃO")