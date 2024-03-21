from Bola.bola import Bola
from Urna.urna import Urna
from Alvo.alvo import Alvo
import random

class Maquina:
    def __init__(self):
        self.definir_valor_bolas()
        self.inserir_bolas_urna()
        self.alvo = Alvo()

    def definir_valor_bolas(self):
        self.bola1 = Bola(1)
        self.bola2 = Bola(2)
        self.bola3 = Bola(3)
        self.bola4 = Bola(4)
        self.bola5 = Bola(5)
        self.bola6 = Bola(6)
        self.bola7 = Bola(7)
        self.bola8 = Bola(8)
        self.bola9 = Bola(9)
        self.bola10 = Bola(10)
        self.bola11 = Bola(11)
        self.bola12 = Bola(12)
        self.bola13 = Bola(13)
        self.bola14 = Bola(14)
        self.bola15 = Bola(15)
        self.bola16 = Bola(16)
        self.bola17 = Bola(17)
        self.bola18 = Bola(18)
        self.bola19 = Bola(19)
        self.bola20 = Bola(20)

    def inserir_bolas_urna(self):
        self.urna = Urna()
        self.urna.adicionar_bola(self.bola1) 
        self.urna.adicionar_bola(self.bola2)
        self.urna.adicionar_bola(self.bola3) 
        self.urna.adicionar_bola(self.bola4) 
        self.urna.adicionar_bola(self.bola5) 
        self.urna.adicionar_bola(self.bola6) 
        self.urna.adicionar_bola(self.bola7) 
        self.urna.adicionar_bola(self.bola8)
        self.urna.adicionar_bola(self.bola9) 
        self.urna.adicionar_bola(self.bola10)
        self.urna.adicionar_bola(self.bola11)
        self.urna.adicionar_bola(self.bola12)
        self.urna.adicionar_bola(self.bola13)
        self.urna.adicionar_bola(self.bola14)
        self.urna.adicionar_bola(self.bola15)
        self.urna.adicionar_bola(self.bola16)
        self.urna.adicionar_bola(self.bola17)
        self.urna.adicionar_bola(self.bola18)
        self.urna.adicionar_bola(self.bola19)
        self.urna.adicionar_bola(self.bola20)       

    def definir_alvo(self):
        self.bola_sorteada = random.choice(self.urna.bolas_disponiveis)
        self.alvo.alvo_atual += self.bola_sorteada.get_bola()
    
    def get_alvo(self):
        return self.alvo.alvo_atual
        