from Palpite.palpite import Palpite

class Jogador:
    def __init__(self):
        self.palpites = []

    def inserir_palpite(self, n_palpite):
        self.palpite = Palpite(n_palpite)

    def armazenar_palpite(self):
        self.palpites.append(self.palpite.get_palpite())

    def get_palpite(self):
        return self.palpite.get_palpite()
        
