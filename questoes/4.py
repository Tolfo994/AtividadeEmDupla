class MochilaDeMissao:
    def __init__(self, agente, equipamentos, capacidade_maxima):
        self.agente = agente
        self.equipamentos = equipamentos
        self.capacidade_maxima = capacidade_maxima

    def adicionar_equipamento(self, equipamento):
        if equipamento != "" and len(self.equipamentos) < self.capacidade_maxima:
            self.equipamentos.append(equipamento)
            print(f"o equipamento {equipamento} foi adicionado")
        else:
            print("equipamento nao adicionado")
        
    def listar_equipamentos(self):
        print("Equipamentos da mochila:")
        for equipamento in self.equipamentos:
            print("-", equipamento)

    def contar_equipamentos(self):
        return len(self.equipamentos)
    
    def verificar_espaco(self):
        if len(self.equipamentos) >= self.capacidade_maxima:
            print("mochila esta cheia")
        else:
            print("pode colocar mais equipamento na mochila")

    def exibir_relatorio(self):
        print("nome do agente:", self.agente)
        print("quantidade de equipamentos:", self.contar_equipamentos())
        print("capacidade maxima:", self.capacidade_maxima)
        print(self.verificar_espaco())


mochila = MochilaDeMissao("cleiton",["lapis", "faca", "espada"],7)

mochila.adicionar_equipamento("leite")
mochila.adicionar_equipamento("radio")
mochila.adicionar_equipamento("arroz")

mochila.listar_equipamentos()

mochila.verificar_espaco()

mochila.exibir_relatorio()





