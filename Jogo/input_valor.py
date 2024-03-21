
class Input_valor:
    def __init__(self):
        self.inserir_valor()
        
    def inserir_valor(self):
        print("Insira um valor")
        self.valor = input()
        self.garantir_numerico()

    def garantir_numerico(self):
        if not self.valor.isdigit():
            print("Digite um valor válido")
            self.inserir_valor()
        else:
            self.valor = int(self.valor)
            self.garantir_intervalo_1_100()
    
    def garantir_intervalo_1_100(self):
        if self.valor > 0 and self.valor < 100:
            pass
        else:
            print("Digite um valor no intervalo de 1 e 100")
            self.inserir_valor()
    
    def get_valor_tratado(self):
        return self.valor