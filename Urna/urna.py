import random

class Urna:
    def __init__(self):
        self.bolas_disponiveis = list(range(1, 21))

    def sortear_bola(self):
        bola_sorteada = random.choice(self.bolas_disponiveis)
        return bola_sorteada

    def sortear_bola_e_atualizar_alvo(self, alvo_anterior):
        nova_bola = self.sortear_bola()
        novo_alvo = alvo_anterior + nova_bola
        return novo_alvo