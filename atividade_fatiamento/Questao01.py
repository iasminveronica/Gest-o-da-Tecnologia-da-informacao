print("QUESTÃO 1:\n Faça um programa que solicite o nome do usuário e imprima-o em formato de escada.\n")

nome = input("Informe seu nome: ")
for i in range(1, len(nome) +1): 
    print(nome[:i])

print("\nFIM DA QUESTÃO")