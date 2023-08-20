
"""
O NUMERO DE CARACTERES (INCLUINDO ESPAÇOS)
NUMERO DE FRASES (HÁ UM PADRÃO, A EPARAÇÃO POR PONTOS AO FINAL DAS FRASESE)
NUMERO DE PALAVRAS (UMA VARIAVEL COM TODAS AS LETRAS DO ALFABETO) count()
QUANTAS VEZES CADA LETRA APARECE (UMA VARIAVEL COM TODAS AS LETRAS DO ALFABETO) count() len()(pq não permite repetições)
"""
enigima = "Hoje é dia de prova de Prog1. A prova está muito fácil. Vou tirar uma boa nota."

print("""
    (=================================================================================)
    (                           ENIGMA COM STRINGS                                    )
    (_________________________________________________________________________________)
    ("Hoje é dia de prova de Prog1. A prova está muito fácil. Vou tirar uma boa nota.")
    ((a)Quantos CARACTERES possui a frase a cima?                                     )
    ((b)Quantas FRASES?                                                               )
    ((c)Quantas PALAVRAS                                                              )
    ((d)Quantas vezes cada LETRA aparece?                                             )
    (=================================================================================)
    """)
total_caracteres = len(enigima)
print(f"(a) Há: {total_caracteres} caracteres!")
num_frases = len(enigima.rstrip('.').split('.'))
print(f"(b)Possuem: {num_frases} frases ao todo!")
total_palavras = len(enigima)
print(f"(c) O total de palavras é:{total_palavras}")
letras_repeticao = enigima.lower().count(enigima)

letras = set(enigima.replace(" ","").replace(".","").lower())
for letra in letras:
    if letra not in '0123456789':
        print(f"(d) {letra} aparece {enigima.lower().count(letra)} vezes.")


