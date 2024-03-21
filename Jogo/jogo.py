from Maquina.maquina import Maquina
from Jogador.jogador import Jogador
from .input_valor import Input_valor
import os

class Jogo:
    def __init__(self):
        self.maquina = Maquina()    
        self.jogador = Jogador()

    def nova_rodada(self):
        self.maquina.definir_alvo()
        self.alvo = self.maquina.get_alvo()

        if self.alvo > 100:
            self.definir_ganhador()

        self.input_tratado = Input_valor()
        self.jogador.inserir_palpite(self.input_tratado.get_valor_tratado())
        self.palpite = self.jogador.get_palpite()

    def comparar_alvo_palpite(self):
        self_vitoria_jogador = True if self.palpite == self.alvo else False 
        return self_vitoria_jogador

    def definir_ganhador(self):
        if self.alvo > 100:
            print("Vitória da máquina :(, o alvo é maior que 100!")
            exit()

        elif self.comparar_alvo_palpite():
            print(f"Parabéns, você ganhou!!! O alvo é {self.maquina.get_alvo()}")
            exit()


        else:
            self.nova_rodada()
            self.definir_ganhador()

