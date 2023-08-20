'''1. Classe Filme: Construa a classe Filme, que obedeça à descrição abaixo:
A classe deve possuir dois atributos: titulo e duracao_em_minutos.
Crie um método exibir_duracao_em_horas que converta o valor em
minutos para horas e apresente a mensagem "O filme TITULO possui X
horas e Y minutos de duração".
Por exemplo, dado o filme com título Titanic que possui 194 minutos de
duração, a mensagem que deverá ser exibida para o usuário será:
"O filme Titanic possui 3 horas e 14 minutos de duração."'''

class Filme():
    def __init__(self, titulo, duracao_em_minutos):
        self.titulo = titulo
        self.duracao_em_minutos = duracao_em_minutos

    #método exibir_duracao_em_horas e apresente a mensagem "O filme TITULO possui X horas e Y minutos de duração
    def exibir_duracao_em_horas(self):
        #194 // 60 =>180
        horas_de_filme = self.duracao_em_minutos // 60                 
        minutos_de_filme = self.duracao_em_minutos - (horas_de_filme*60)
        print(f"Convertendo...\nO filme {self.titulo} tem: {horas_de_filme} horas e {minutos_de_filme} minutos de duração")
    
#main:
filme1 = Filme("Titanic",194)
print(f"O filme {filme1.titulo} tem: {filme1.duracao_em_minutos} minutos")

filme1.exibir_duracao_em_horas()

filme2 = Filme("DOA- Vivo ou Morto", 87)
print(f"\nO filme {filme2.titulo} tem: {filme2.duracao_em_minutos} minutos")

filme2.exibir_duracao_em_horas()