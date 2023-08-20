print("Questão 08\n\n -O ano Bissexto ou Não?-")
calendarioAnual = int(input("Insira apenas o ano da data que deseja consultar: \n"))

#terminações em 00
if calendarioAnual %400==0:
    print(f"O ano {calendarioAnual} é ano Bissexto!")
# ou a dezena for divisivel por 4
elif calendarioAnual %4 ==0:
      print(f"O ano {calendarioAnual} é ano Bissexto!")
else:
     print(f"{calendarioAnual} Não é ano Bissexto")