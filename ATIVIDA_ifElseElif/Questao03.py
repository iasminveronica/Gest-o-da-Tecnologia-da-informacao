print("Questão 03\n\n")

# comandos de entrada para receber os números
num1 = float(input("Insira um número qualquer: "))
num2 = float(input("Insira um número qualquer: "))
num3 = float(input("Insira um número qualquer: "))

# variávei para comparação - necessário, pois vou usar o and para otimizar o código, se não a cadeia de condição ia ficar muito grande
maiorNumero = num3
menorNumero = num3

# Estrutura de condição para mostrar o maior número entre os 3 
if num1 > maiorNumero and num2:
    print(f"{num1} é o maior numero informado  ")
elif num2 > maiorNumero and num1:
    print(f"{num2} é o maior númeor informado")
else:
    print(f"{num3} é o maior número informado")

# Estrutura de condição para mostrar o menor número entre os 3 
if num1 < menorNumero and num2:
    print(f"{num1} é o menor numero informado  ")
elif num2 < menorNumero and num1:
    print(f"{num2} é o menor númeor informado")
else:
    print(f"{num3} é o menor número informado")


