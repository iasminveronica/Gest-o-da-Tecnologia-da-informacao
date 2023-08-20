print("QUESTÃO 7:\
Faça um programa que receba uma palavra e a imprima de trás-para-frente \
(letra por letra)")

palavra = input("Informe uma palavra: ")
for i in range(1, len(palavra), 1):
    print(palavra[-i])

print("\n\n\n\n--------------------------")
if palavra ==  palavra:
    print("FIM DA QUESTÃO")