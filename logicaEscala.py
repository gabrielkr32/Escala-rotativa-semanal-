import itertools
#Importação garenta que quando chegarmos ao final da lista de personagens ela começara novamente


   #teste inicial:
   #Dias_semana: é uma lsita de dias da semana para atribuir os personagens
   #Personagens: lista para atribuir aos 'Dias_semana'

def gerar_escala(dias_semana, personagens):
        iter_personagens = itertools.cycle(personagens) #usando itertools.cycle para atribuir periodicamente personahens aos dias
        
        escala_semanal = {}
        for dia in dias_semana:
                #'refaz' sobre cada dia, para obter o proximo personagem 
                personagem = next(iter_personagens)
                escala_semanal[dia] = personagem

        return escala_semanal 
#Função 'gerar_escala': recebe 'dias_semana' e 'personagens' como parametros.  


def main():
        #Executa o teste, chama 'gerar-escala' com os dias da semana e personagens fornecidos
        dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
        personagens = ["Personagem A", "Personagem B", "Personagem C"]

        escala = gerar_escala(dias_semana, personagens)
        
        #mostrando a escala gerada
        for dia, personagem in escala.items():
                print(f'{dia}: {personagem}')


if __name__ == '__main__':
        main()


