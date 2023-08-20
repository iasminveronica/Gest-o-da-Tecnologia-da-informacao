print("QUESTÃO 8:\
Faça um programa que receba do usuário uma string.\
O programa imprime a string sem suas vogais.")

frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU" 
for i in range(len(vogais)): 
    frase = frase.replace(vogais[i],"")  
print(frase) 
print("\n\n--------------------------")
print("FIM DA QUESTÃO")