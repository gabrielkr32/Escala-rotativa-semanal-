import itertools
#Importação garenta que quando chegarmos ao final da lista de personagens ela começara novamente


   #teste inicial:
   #Dias_semana: é uma lsita de dias da semana para atribuir os personagens
   #Personagens: lista para atribuir aos 'Dias_semana'

def gerar_escala(dias_semana, personagens, artistas_Masc, artistas_Fem):
        iter_personagens = itertools.cycle(personagens) #usando itertools.cycle para atribuir periodicamente personahens aos dias
        
        escala_semanal = {}
        for dia in dias_semana:
                #'refaz' sobre cada dia, para obter o proximo personagem 
                personagem = next(iter_personagens)
                
                if personagem == "Possuida":
                        artista = next(iter(artistas_Fem))
                else:
                        artista = next(iter(artistas_Masc))        

                escala_semanal[dia] = (personagem, artista)

        return escala_semanal

def main():
        #Executa o teste, chama 'gerar-escala' com os dias da semana e personagens fornecidos
        dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
        personagens = ["Mordomo","Mestre", "Dracula", "Prisioneiro", "Necroterio", "Possuida", "Cemiterio", "Trevas"]
                          #adicionei os nomes dos personagens para organização na escala em teste mais proximo do real
        #criando uma lista dos artista separados por genero
        artistas_Masc = ["Darlei", "Jhony", "Paulo", "Gabriel", "Matheus", "Douglas", "Kevin"]
        artistas_Fam = ["Monica", "Janine", "Barbara"]
        #uma regra a ser seguida é: um personagem feminino com um artista feminino.
        
        
        escala = gerar_escala(dias_semana, personagens, artistas_Masc, artistas_Fam)
        
        #mostrando a escala gerada
        for dia, (personagem, artista) in escala.items():
                print(f'{dia}: {personagem} - {artista}')


if __name__ == '__main__':
        main()


