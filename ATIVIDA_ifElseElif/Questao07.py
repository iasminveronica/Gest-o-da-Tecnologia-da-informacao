print("Questão 07\n\n -Meses do Ano-")

calendarioMensal = int(input("Insira um número de 1 a 12 referente ao mês que deseja consultar:\n"))
calendario = 1,2,3,4,5,6,7,8,9,10,11,12

if calendarioMensal == 1:
    print("JANEIRO é o primeiro mês do ano no calendário Greforiano e possui 31 dias")
elif calendarioMensal ==2:
    print("FEVEREIRO é o segundo mês do ano e possui apenas 28 dias \n -* Sendo de responsabilidade dos egípcios de Alexandria o calculo para a distribuição dos dias que tal mês possui")
elif calendarioMensal == 3:
    print ("MARÇO é o 3° mês do ano e tem 31 dia!")
elif calendarioMensal == 4:
    print ("ABRIL é o 4° mês do ano e tem 30 dias!")
elif calendarioMensal == 5:
    print ("MAIO é o 5° mês do ano e tem 31 dias!")
elif calendarioMensal == 6:
    print ("JUNHO é o 4° mês do ano e tem 30 dias! \nCom fé nos estudos de domingo já estarei passada nessa matéria, amém?")
elif calendarioMensal == 7:
    print ("JULHO é o 7° mês do ano e tem 31 dias!")
elif calendarioMensal == 8:
    print ("AGOSTO é o 8° mês do ano e tem 31 dias!")
elif calendarioMensal == 9:
    print ("SETEMBRO é o 9° mês do ano e tem 30 dias!")
elif calendarioMensal == 10:
    print ("Outubro é o 10° mês do ano e tem 31 dias!")
elif calendarioMensal == 11:
    print ("NOVEMBRO é o 11° mês do ano e tem 30 dias!")
# Queria colocar a extensão do power mode, mas meu notebook ia pegar fogo junto
elif calendarioMensal == 12:
    print ("DEZEMBRO é o 12° mês do ano e tem 31 dias! \n Feliz Festas de Final de Ano ")
elif calendarioMensal != calendario:
    print(f"404 ERRO \n Código inválido! {calendarioMensal} não é referente a mês algum! TENTE NOVAMENTE")

