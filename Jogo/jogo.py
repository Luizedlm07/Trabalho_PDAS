from Urna.urna import Urna

class Jogo:
    def __init__(self):
        self.urna = Urna()
        self.alvo = None

    def iniciar_jogo(self):
        self.alvo = self.urna.sortear_bola()
        return self.alvo

    def jogar(self, palpite):
        if palpite == self.alvo:
            return True
        else:
            self.alvo = self.urna.sortear_bola_e_atualizar_alvo(self.alvo)
            return False  