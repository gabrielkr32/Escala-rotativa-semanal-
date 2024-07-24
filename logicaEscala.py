import itertools

class Personagem:
        def __init__(self, nome, genero):
                self.nome = nome
                self.genero = genero


class Escala:
        def __init__(self, personagens):
                self.personagens = personagens
                self.escala_semanal = {}


def gerar_escala(dias_semana, personagens, artistas_Masc, artistas_Fem):
        iter_personagens = itertools.cycle(personagens) 
        iter_artistas_Masc = itertools.cycle(artistas_Masc)
        iter_artistas_Fem = itertools.cycle(artistas_Fem)

        escala_semanal = {}
        for dia in dias_semana:
                escala_dia = {}
                
                for personagem in personagens:
                        if personagem == "Possuida":
                                artista = next(iter_artistas_Fem)
                        else:
                            artista = next(iter_artistas_Masc)        
                            
                        escala_dia[personagem] = artista

                escala_semanal[dia] = escala_dia

        return escala_semanal        

def main():
        dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
        personagens = ["Mordomo","Mestre", "Dracula", "Prisioneiro", "Necroterio", "Possuida", "Cemiterio", "Trevas"]
                          
        artistas_Masc = ["Darlei", "Jhony", "Paulo", "Gabriel", "Matheus", "Douglas", "Kevin"]
        artistas_Fam = ["Monica", "Janine", "Barbara"]
        
        escala = gerar_escala(dias_semana, personagens, artistas_Masc, artistas_Fam)
        
        for dia, escala_dia in escala.items():
           print(f'{dia}:')
           for personagem, artista in escala_dia.items():
               print(f'    {personagem} - {artista}')


if __name__ == '__main__':
        main()


