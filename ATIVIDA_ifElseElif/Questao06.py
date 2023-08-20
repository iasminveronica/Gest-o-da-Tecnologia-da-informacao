print("Questão 06\n\n -Dias da Semana-")

calendario = int(input("Que dia da semana é hoje? Insira um número de 1 a 7 referente ao dia da semana:\n"))

if calendario ==1:
    print("Domingo - dia de estudar python. Professor Caio, as atividades têm que ser feita aos domingos")
elif calendario == 2:
    print("Segunda-feira")
elif calendario == 3:
    print("Terça-feira")
elif calendario == 4:
    print("Quarta-feira")
elif calendario == 5:
    print("Quinta-feira")
elif calendario == 6:
    print("Sexta-feira")
elif calendario == 7:
    print("Sábado")
elif calendario != 1 or 2 or 3 or 4 or 5 or 6 or 7:
    print(f"404 ERRO\n Valor Inválido - não há dias da semana referente a {calendario} ") 
