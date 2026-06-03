class RoboColetor:
    def __init__(self, nome, amostras, capacidade_maxima):
        self.nome=nome
        self.amostras=amostras
        self.capacidade_maxima=capacidade_maxima

    def adicionar_amostra(self,amostra):
        if amostra == " ":
            print("não pode estar escrito nada")
        elif len(self.amostras)>= self.capacidade_maxima:
            print ("Armazenamento Cheio")
        else:
            self.amostras.append(amostra)
            print(f"{amostra} adicionada")

    def listar_amostras(self):
        if len(self.amostras)==0:
            print("nenhuma amostra foi coletada")
        else:
            print("as mostras coletadas foram:")
            for amostra in self.amostras:
                print(f" -{amostra}")

    def contar_amostras(self):
        return len(self.amostras)
    
    def verificar_armazenamento(self):
        if len(self.amostras)>= self.capacidade_maxima:
            print ("armazenamento esta cheio")
        else:
            espacos=self.capacidade_maxima - len(self.amostras)
            print(f"armazenamento com {espacos} disponiveis")

    def exibir_relatorio(self):
        print(f"robô: {self.nome}")
        print(f"amostras coletadas: {self.contar_amostras()}")
        print(f"capacidade maxima:{self.capacidade_maxima}")
        self.verificar_armazenamento()
        self.listar_amostras()

r=RoboColetor("ganso",[],4)
r.adicionar_amostra("red")
r.adicionar_amostra("blue")
r.adicionar_amostra(" ")

print(r.exibir_relatorio())



