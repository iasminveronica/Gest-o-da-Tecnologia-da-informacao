print("Questão 04\n\n -SEBO LITERÁRIO - COLEÇÃO AGATHA CHRISTIE-")

print(" =================CAIXA==================== \n")

livro01 = float(input("O valor do livro 'Café Preto' é: R$ "))
livro02 = float(input("O valor do livro 'Morte no Nilo' é: R$ "))
livro03 = float(input("O valor do livro 'O assassinato no expresso do oriente' é: R$ "))

livro1 = str("Café preto")
livro2 = str("Morte no Nilo")
livro3 = str("Assassinato no Expresso do Oriente")

produtoMaisBarato = livro03

#tenho que economizar:
if livro01 < produtoMaisBarato and livro02:
    print(f" Oba! {livro1} era o livro que eu quria ler mesmo!")
elif livro02 < produtoMaisBarato and livro01:
     print(f" Oba! {livro2} era o livro que eu quria ler mesmo!")
else:
    print(f" Oba! {livro3} era o livro que eu quria ler mesmo!")

