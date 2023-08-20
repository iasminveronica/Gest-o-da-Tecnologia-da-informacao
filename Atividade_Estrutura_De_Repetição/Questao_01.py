lista_numeros = []
print("""
    \INT KEYBOARD - ON/
    """)
numero = int
while numero != 'N':

    pergunta = input(''' 
        |Deseja adicionando um número?
        |(S) Sim
        |(N) Não
            ''').upper()
    if pergunta == 'S':
        numero = int(input("Informe outro número inteiro: "))
        lista_numeros.append(numero)
    else:
        break
pares = numero % 2 == 0
if numero == pares:
    print(f"Os números pares informados são: {pares}")







