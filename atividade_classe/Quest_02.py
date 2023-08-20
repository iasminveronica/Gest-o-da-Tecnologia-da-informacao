'''
2. Classe Conta Corrente: Crie uma classe para implementar uma conta
corrente.
A classe deve possuir os seguintes atributos: número da conta, nome do
correntista e saldo. Os métodos são os seguintes: alterar_nome, deposito e
saque;
No construtor, saldo é opcional, com valor default (padrão) zero e os demais
atributos são obrigatórios.
'''

class Corrente:
    def __init__(self,numero_da_conta,nome_correntista, saldo=0):
        self.numero_da_conta = numero_da_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self):
        print("="*25,"BANCO IF","=" *25)
        novo_nome = input("Informe seu nome: ")
        self.nome_correntista = novo_nome
        print(f"Novo nome{novo_nome}")

    def depositar(self):
        while True:
            print("="*25,"DEPOSITO","="*25)
            valor_deposito = float(input("Valor que deseja depositar:\nR$ "))
            if valor_deposito <= self.saldo:
                print("Valor inválido!")
                print("=" *50)
            elif valor_deposito >= self.saldo:
                self.saldo +=  valor_deposito
                print(f"Deposito no valor de R${valor_deposito} efetuado com sucesso!")
                break

    def sacar(self): 
        while True:
            print("="*26,"SAQUE","="*26)
            valor_saque = float(input("Valor que deseja sacar:\nR$ "))
            print("=" *30,"="*30)
            if valor_saque > self.saldo:
                print("Valor inválido!")
            elif valor_saque <= self.saldo:
                self.saldo -=  valor_saque
                print(f"Deposito no valor de R${valor_saque} efetuado com sucesso!\nSaldo em conta: {self.saldo}")  
                print("="*21,"FINAL DA OPERAÇÃO","="*21)  
                break

#main
conta_corrente1 = Corrente(132456, "Iasmin")

conta_corrente1.alterar_nome()
conta_corrente1.depositar()
conta_corrente1.sacar()


