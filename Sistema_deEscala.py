import itertools

class Personagem:
    def __init__(self,nome,genero):
        self.nome = nome 
        self.genero - genero 
    
class Escala:
    def __init__(self,personagens):
        self.personagens = personagens
        self.escala_semanal = [] 

    def gerar_escala(self):
        #implementar a logica para gerar uma escala 
        # exmplo basico para ilustrar
        # dias_semana = ['segunda', 'terça', 'quarta'....] 
        escala = []   