numeros = []

for i in range(10):
    num = int(input(f"Informe {i}° número: "))
    numeros.append(bin(num)[2:])
for binario in numeros:
    print(binario)