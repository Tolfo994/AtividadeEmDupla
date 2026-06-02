class CapsulaDoTempo:
    def __init__(self, autor, mensagem, ano_abertura, ano_atual):
        self.autor=autor
        self.mensagem=mensagem
        self.ano_abertura=ano_abertura
        self.ano_atual=ano_atual

    def pode_abrir(self):
        if self.ano_atual>=self.ano_abertura:
            return (f"A capsula foi aberta e sua mensagem é {self.mensagem}, escrita por {self.autor}")
        else:
            return ("ainda você não pode abrir a capsula")
    
    def calcular_espera(self):
        falta=self.ano_abertura-self.ano_atual
        if falta<=0:
            return "falta 0 anos"
        else:
            return f"falta {falta} anos"
    
    def calssificar_espera(self):
        falta=self.ano_abertura-self.ano_atual
        if falta==0:
            return "Pode abrir agora"
        elif falta <= 3 :
            return "espera curta"
        else:
            return "espera longa"
        
user= CapsulaDoTempo("Gustavo Anversa","eduardo pizza",2050,2020)
print(user.autor)
print(user.ano_abertura)
print(user.calcular_espera())
print(user.calssificar_espera())
print (user.pode_abrir())