from random import randint
import pygal


class um_dado:
    '''Classe que vai mostrar um dado'''
    def __init__(self, numero_lados=6):
        '''define o dado com apenas 6 lados'''
        self.numero_lados = numero_lados

    def rolar_dado(self):
        '''retorna o valor aleatorio de 1 ate 6 (numero de lados)'''
        return randint(1, self.numero_lados)

    def Iniciar(self, ):
       
        self.CriarERolar()
        self.criar_grafico()
       


    def CriarERolar(self):
         # CRIA UM DADO DE 6 LADOS  
        dado_principal = um_dado()
        
        #rola o dado algumas vezes e armazena as informações
        roladas = [] 
        for numero_lancadas in range(1000):
            resultado = self.rolar_dado()
            roladas.append(resultado)
        
    # Analisa a frequencia que cada numero é escolhido
        self.frequencias = []
        for valor in range(1, self.numero_lados + 1):
            frequencia = roladas.count(valor)
            self.frequencias.append(frequencia)
    
    
    def criar_grafico(self):
         # Mostra os resultados
        hist = pygal.Bar()
        
        
        hist.title = 'Analisando um dado sendo lançando 1000 vezes'
        hist.x_labels = ['1', '2', '3', '4', '5', '6']
        hist.x_title = "Resultado"
        hist.y_title = "Frequencia dos lançamentos"

        hist.add('dado', self.frequencias)
        hist.render_to_file('Visualização_do_dado.svg')



comecar = um_dado()
comecar.Iniciar()