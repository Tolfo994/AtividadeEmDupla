class PortalDimensional:
    def __init__(self,nome,destino,energia_necessaria,energia_disponivel):
        self.nome = nome
        self.destino = destino
        self.energia_necessaria = energia_necessaria
        self.energia_disponivel = energia_disponivel

    
    def pode_abrir(self):
        if self.energia_disponivel >= 100:
            return "portal aberto"
        elif self.energia_disponivel < 100:
            return "energia insuficiente portal vai ter que ficar fechado"

    def calcular_falta_energia(self):
        if self.energia_necessaria - self.energia_disponivel == 0:
            return 0
        else:
            return "falta:", self.energia_necessaria - self.energia_disponivel, "de energia"

    def classificar_estabilidade(self):
        if self.energia_disponivel >= 100:
            print("portal estavel")
        elif self.energia_disponivel >= 80:
            print("portal quase estavel")
        elif self.energia_disponivel < 80:
            print("portal instavel")
        
    def exibir_resumo(self):
        print("nome do poral",self.nome)
        print("destino:", self.destino)
        print("energia disponivel", self.energia_disponivel)
        print("enegia necessaria", self.energia_necessaria)
        if self.energia_disponivel >= 100:
            print("Situação do portal: estavel")
        elif self.energia_disponivel >= 80:
            print("Situação do portal: quase estavel")
        elif self.energia_disponivel < 80:
            print("Situação do portal: portal instavel")

    


portal = PortalDimensional("Buracos de Minhoca","universo 10",100,50)

print(portal.pode_abrir())

print(portal.calcular_falta_energia())

portal.classificar_estabilidade()

portal.exibir_resumo()