print("Questão 10\n\n -Nomes de Triângulos-")

baseDoTrangulo = float(input("Informe o valor da base do triângulo: "))
ladoA = float(input("Informe o valor do lado A do triângulo: "))
ladoB = float(input("Informe o valor do lado B do triângulo: "))

eUmTriangulo =  baseDoTrangulo + ladoA > ladoB 
triEquilatero = baseDoTrangulo == ladoA == ladoB
triIsoceles = baseDoTrangulo == ladoA or baseDoTrangulo == ladoB or ladoB == ladoA
triEscaleno = baseDoTrangulo != ladoA  or baseDoTrangulo != ladoB or ladoB != ladoA 

if  eUmTriangulo and triEquilatero:
    print("Os valores podem formar um triângulo e ele é um Triângulo Equilátero! ")
elif eUmTriangulo and triIsoceles:
    print("Os valores podem formar um triângulo e ele é um Triângulo Isósceles! ")
elif eUmTriangulo:
    print("Os valores podem formar um triângulo e ele é um Triângulo Escaleno! ")
else:
    print("ERRO 4040 \nOs valores informados não formam um tirângulo! \nTalvez o triângulo das Bermudas")


