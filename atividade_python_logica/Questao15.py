# a.	salário bruto.
# b.	quanto pagou ao INSS.
# c.	quanto pagou ao sindicato.
# d.	o salário líquido.e.	calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# 	IR (11%)	R$
# 	INSS (8%)	R$
#   Sindicato ( 5%)
# 	Salário Liquido	R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.
# +
# #
valorhora = float(input("\nQuanto você recebe por horas trabalhadas? "))
horasTrabalhadas = float(input("Quantas horas você trabalha por mês, ou trabalhou no ultmino mês? "))

# SalarioBruto
salario = valorhora * horasTrabalhadas
print("Seu salário bruto é: R$", salario)

# INSS
print("Valor pago ao INSS: R$", (salario + (8/100)  * salario) - salario)

#Sindicato
print("Valor pago ao sindicato: R$", (salario + (5/100) * salario ) - salario)

# desconto = salario - 25/100
print("Seu salário líquido é: R$" ,( salario - (25/100) * salario ))

