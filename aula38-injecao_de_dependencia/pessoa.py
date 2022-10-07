class Pessoa:
    def __init__(self, comportamento):
        self.comportamento = comportamento
    
    def realizar_acao(self):
        self.comportamento.acao()