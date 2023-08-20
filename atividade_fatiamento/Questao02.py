print("QUESTÃO 1:\n Faça um programa que lê uma string e imprime “Palíndromo” caso a string seja um \
palíndromo e “Não é palíndromo”, caso não seja.\n")

palavra = input("Informe uma palavra: ")
palavra = palavra.replace(" ","")
if palavra == palavra[: : -1]:
    print("é um Palíndromo")
else:
    print("Não é um Palíndromo")

print("\n\n\n\n--------------------------")
print("FIM DA QUESTÃO")