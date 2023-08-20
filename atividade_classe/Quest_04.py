'''4. Classe Carro: Implemente uma classe chamada Carro com as seguintes propriedades:
Um veículo tem um certo consumo de combustível (medido em km / litro) e uma certa quantidade de combustível no tanque;
O consumo é especificado no construtor e o nível de combustível inicial é 0;
Forneça um método andar() que simule o ato de dirigir o veículo por
uma certa distância, reduzindo o nível de combustível no tanque de gasolina;
Forneça um método obter_gasolina(), que retorna o nível atual de combustível;
Forneça um método adicionar_gasolina(), para abastecer o tanque.
Exemplo de uso:
meuFusca = Carro(15); # 15 quilômetros por litro de combustível.
meuFusca.adicionarGasolina(20);
 # abastece com 20 litros de combustível.
meuFusca.andar(100); 
# anda 100 quilômetros.
meuFusca.obterGasolina()
# Imprime o combustível que resta no tanque.'''


class Carro():
    def __init__(self, consumo_de_combustivel,quantidade_combustive_tanque=0):
        self.consumo_de_combustivel = consumo_de_combustivel
        self.quantidade_combustive_tanque = quantidade_combustive_tanque

    def andar(self, km):
        if self.quantidade_combustive_tanque * self.consumo_de_combustivel >= km:
            combustivel_consumido = km / self.consumo_de_combustivel
            self.quantidade_combustive_tanque -= combustivel_consumido
            print(f"O carro rodou {km:.2f}km \n")
        else:
            print("Carro sem combustivel!")
            
    def obter_combustivel(self):
       print(f"Combustível atual: {self.quantidade_combustive_tanque:.2f} L\n")

    def adicionar_combustivel(self, abastecendo_tanque):
       self.quantidade_combustive_tanque += abastecendo_tanque
       print(f"Combustível atual: {self.quantidade_combustive_tanque:.2f} L\n")

#main
meuFusca = Carro(15)
meuFusca.adicionar_combustivel(20)
meuFusca.andar(100)
meuFusca.obter_combustivel()