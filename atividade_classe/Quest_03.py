'''3. Classe Bomba de Combustível: Faça um programa completo utilizando
uma classe chamada BombaCombustivel, com no mínimo esses atributos:
tipo_combustivel, valor_litro e quantidade_combustivel;
Possua no mínimo esses métodos:
abastecer_por_valor( ) – método onde é informado o valor a ser
abastecido e mostra a quantidade de litros que foi colocada no veículo;
abastecer_por_litro( ) – método onde é informado a quantidade em
litros de combustível e mostra o valor a ser pago pelo cliente;
alterar_valor( ) – altera o valor do litro do combustível;
alterar_combustivel( ) – altera o tipo do combustível;
alterar_quantidade_combustivel( ) – altera a quantidade de combustível
restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a
quantidade de combustível total na bomba.'''


class Bomba_de_combustivel():
    def __init__(self,tipo_combustivel, valor_litro, quantidade_combustivel):
        
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

#altera a quantidade de combustível restante na bomba.
    def alterar_quantidade_combustivel(self, quantidade):
        self.quantidade_combustivelcombustivel += quantidade
        print(f"Há {self.quantidade_combustivel} L de combustivel na bomba" )


#informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente;
    def abastecer_por_litro(self, litros):
        #certificando que a quantidade me litros é maior que zero e <= a quantidade de combustivel na bomba
        if litros > 0 and litros <= self.quantidade_combustivel:
            valor_pago = litros * self.valor_litro
            self.quantidade_combustivel -= litros
            print(f"R${valor_pago} | {litros}L")
        else:
            print("Quantidade de litros invalida para abastecimento!")

#informar o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
    def abastecer_por_valor(self, valor_abastecido):
        if valor_abastecido > 0:
            litros = valor_abastecido / self.valor_litro
            self.abastecer_por_litro(litros)
        else:
            ("Valor invalido para abastecimento!")
            
#altera o valor do litro do combustível
    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor
        print(f"Valor {self.tipo_combustivel} alterado!\nNovo valor: R${novo_valor:.2f}")
                    
# altera o tipo do combustível
    def alterar_combustivel(self, alterar_tipo_de_combustivel):
        if alterar_tipo_de_combustivel == "Diesel":
            self.tipo_combustivel = alterar_tipo_de_combustivel
        elif alterar_tipo_de_combustivel == "alcool":
            self.tipo_combustivel = alterar_tipo_de_combustivel
        elif alterar_tipo_de_combustivel == "Etanol":
            self.tipo_combustivel = alterar_tipo_de_combustivel
        else:
            print("Combustivel inválido!")

#main
bomba1 = Bomba_de_combustivel("diesel",2.5, 10)
bomba1.alterar_combustivel("alcool")
bomba1.alterar_valor(5)
bomba1.abastecer_por_litro(8)
bomba1.valor_litro