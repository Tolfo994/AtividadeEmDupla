class MochilaDeMissao:
    def __init__(self, agente, equipamentos, capacidade_maxima):
        self.agente = agente
        self.equipamentos = equipamentos
        self.capacidade_maxima = capacidade_maxima

    def adicionar_equipamento(self, equipamento):
        equipamento = input("Informe um equipamento que voce quer colocar:")
        self.equipamentos.append(equipamento)
        print(f"Equipamento {equipamento} adicionado com sucesso!")

    


mochila = MochilaDeMissao("cleiton","lapis" "faca",2)

mochila.adicionar_equipamento(2)



