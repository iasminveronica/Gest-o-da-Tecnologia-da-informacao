mensagem = []
controle = 0
while controle != "0":
    orientacao = (input("""
        |||||||||||||||||||||||||||||||||||||||||||||
        |==========Zap_Barraca_Code===============  |
        |Para sair do sistema basta precionar "0"   |
        |Para ir até a Caixa de Texto precione enter|
        |                                           |
        |===========================================|
        \n"""))
    if orientacao != "0":
        mensagens = input("Digite uma mensagem\n:")
        #o usuário escrever uma mensagem na tela e guarde tudo em uma string.
        mensagem.append(mensagens)
        print("Mensagem enviada!")
    #A escrita só vai parar quando o usuário entrar com o caractere “0”;
    elif orientacao == "0":
            break
#Logo após, mostre a string gerada.
print(f"Histórico de mensagens: {mensagem}")
