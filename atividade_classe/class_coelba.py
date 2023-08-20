class Coelba:
    def __init__(self, cnpj,endereco):
        self.cnpj = cnpj
        self.endereco = endereco

class Contrato:
    def __init__(self, nome_cliente, endereco_cliente, cpf):
        self.nome_cliente = nome_cliente
        self.endereco_cliente = endereco_cliente
        self.cpf = cpf

class Boleto:
    def __init__(self):
        self.imprimir_boleto = []  
    
    def imprime(self):
       print("-"*10,"NEOENERGIA","-"*10,"\n",
             "-"*10,"coelba","-"*10) 
       for im_vertical in self.imprimir_boleto:
        print(im_vertical)
     

class Servico_Energia:
    def __init__(self, contrato_cliente):
        self.contrato_cliente = contrato_cliente
        self.consumo_energia = 0
        self.taxa_watt = 10 
        self.ilum_publica = 6
        self.multa_nf = 1.08
        self.juros_nf = 0.63
        self.ipca_nf = 0.37
        self.boleto = Boleto()
    
    def consu_luz(self, kwh):
        if kwh > 10000:
            self.consumo_energia = kwh * 0.32168577 + self.taxa_watt + self.ilum_publica + self.multa_nf + self.ipca_nf
        else:
            self.consumo_energia = kwh * 0.32168577 + self.ilum_publica + self.multa_nf + self.ipca_nf
    
        self.boleto.imprimir_boleto.append(f"NOME DO CLIENTE:{self.contrato_cliente.nome_cliente}\nCPF:{self.contrato_cliente.cpf}\nENDEREÇO:{self.contrato_cliente.endereco_cliente}")
        self.boleto.imprimir_boleto.append(f"CONSUMO:{kwh} kwh")      
        self.boleto.imprimir_boleto.append(f'\nIluminação pública:{self.ilum_publica}\nMulta-NF: {self.multa_nf}\nJuros-NF:{self.juros_nf}\nIPCA-NF:{self.ipca_nf}\nTOTAL A PAGAR:R${self.consumo_energia:.2f}')


cliente1 = Contrato("Iasmin","Rua_bla",1234)
servico1 = Servico_Energia(cliente1)

servico1.consu_luz(291.56)
servico1.boleto.imprime()