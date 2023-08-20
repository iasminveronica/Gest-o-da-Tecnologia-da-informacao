print("Questão 05\n\n -Horário das Aulas-")

#str para receber um caractere como valor (não acertei usar o format no input (pode?), por isso coloquei essas variáveis ) -
turnoDaAula = str(input("Informe qual turno você estuda, insira: \n(M) caso seja no período Matutino;\n(V) para o Vespertino; \n(N) para o Noturno \n =>")) 


#variaveis para fazer as condições (se caso o usuário coloquar a letra em maiúsculo o código também vai rodar ) -
m = str("M")
v = str("V")
n = str("N")

if turnoDaAula == m:
    print("Bom Dia!")
elif turnoDaAula == v:
    print("\nBoa Tarde!")
elif turnoDaAula == n:
    print("Boa Noite!")
#diferente aos valores pedidos é necessário reportar fedback de erro -
elif turnoDaAula != m or n or v:
    print("ERRO 404 \n Valor Invalido")

