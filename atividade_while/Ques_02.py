"""
input
nome de cidades = str
n° de habitantes = int 
pelo menos 10 cidades = while
qual a cidade mais populosa if cidade a > cidade b = print(cidade + numero de habitantes) 
pesquisar #index?
"""
nome_cidade = []
num_habitantes = []
maior = 0
while nome_cidade != "fim":
    cidades = input(""" 
        (|___________________________________________|)
        (|               IBGE_CODE                   |)
        (|___________________________________________|)
        (|Pesquisa Populacional  - A seguir:         |)
        (|Informe o nome de pelo menos 10 cidades    |)
        (|Ao final da pesquisa digite "fim" para sair|)
        (|___________________________________________|)
         \n:""")

    if cidades == "fim":
        break
    nome_cidade.append(cidades)

    numero_cidadoes = int(input("""
        (|___________________________________|)
        (|Informe o n° populacional da cidade|)
        (|___________________________________|)
        \n:"""))
    num_habitantes.append(numero_cidadoes)
   
maior = max(num_habitantes)
maior_cidade = num_habitantes.index(maior)
print(f"Cidade mais populosa: {nome_cidade[maior_cidade]} sendo seu n°: {maior} ")