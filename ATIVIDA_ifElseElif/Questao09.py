print("Questão 09\n\n -Nadadores e Idades-")

print("Questionário para o IBGE:")
idade = int(input("Qual a idade do nadador: "))

if  idade >=5 and idade <=7 :
    print(f"O nadador anônimo tem {idade}, logo se enquadra na categoria 'INFANTIL A' ")
elif idade >=8 and idade <=10 :
    print(f"O nadador anônimo tem {idade}, logo se enquadra na categoria 'INFANTIL B' ")
elif idade >=11 and idade <=13 :
    print(f"O nadador anônimo tem {idade}, logo se enquadra na categoria 'JUVENIL A' ")
elif idade >=14 and idade <=17 :
    print(f"O nadador anônimo tem {idade}, logo se enquadra na categoria 'JUVENIL B ")
elif idade >= 18 :
    print(f"O nadador anônimo tem {idade}, logo se enquadra na categoria 'ADULTO' ")
