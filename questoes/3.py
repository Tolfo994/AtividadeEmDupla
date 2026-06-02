class RoboColetor:
    def __init__(self, nome, amostras, capacidade_maxima):
        self.nome=nome
        self.amostras=amostras
        self.capacidade_maxima=capacidade_maxima

    def adicionar_amostra(self,amostra):
        if amostra != "":
            print("não pode estar escrito nada")
        elif len(self.amostras)>= self.capacidade_maxima:
            print ("Armazenamento Cheio")
        else:
            self.amostras.append(amostra)
            print(f"{amostra} adicionada")

    def listar_amostras(self):
        

