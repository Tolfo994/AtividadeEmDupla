class TorneioDeDrones:
    def __init__(self, nome_torneio, provas, bateria_inicial):
        self.nome_torneio = nome_torneio
        self.provas = provas
        self.bateria = bateria_inicial
        self.pontos = 0
        self.provas_concluidas = []

    def listar_provas(self):
        for i, prova in enumerate(self.provas):
            print(i, "-", prova["nome"], "-", prova["custo"], "-", prova["pontuacao"])

    def tentar_prova(self, numero_prova):
        if numero_prova < 0 or numero_prova >= len(self.provas):
            print("prova inválida")
            

        prova = self.provas[numero_prova]

        if prova["nome"] in self.provas_concluidas:
            print("prova já concluída")
        elif self.bateria >= prova["custo"]:
            self.bateria -= prova["custo"]
            self.pontos += prova["pontuacao"]
            self.provas_concluidas.append(prova["nome"])
            print("prova concluída com sucesso")
        else:
            print("bateria insuficiente")

    def calcular_progresso(self):
        return len(self.provas_concluidas)

    def verificar_situacao(self):
        if len(self.provas_concluidas) == len(self.provas):
            return "torneio concluído"
        elif self.bateria == 0:
            return "torneio encerrado sem bateria"
        else:
            return "torneio em andamento"

    def exibir_relatorio(self):
        print("torneio:", self.nome_torneio)
        print("bateria restante:", self.bateria)
        print("pontos:", self.pontos)
        print("provas concluídas:", self.provas_concluidas)
        print("situação:", self.verificar_situacao())


# Exemplo de uso

provas = [
    {"nome": "zigue-zague aéreo", "custo": 20, "pontuacao": 30},
    {"nome": "túnel de precisão", "custo": 15, "pontuacao": 25},
    {"nome": "corrida vertical", "custo": 10, "pontuacao": 20}
]

torneio = TorneioDeDrones("desafio dos Drones", provas, 50)

torneio.listar_provas()

torneio.tentar_prova(0)

torneio.tentar_prova(1)

torneio.tentar_prova(2)

print("progresso:", torneio.calcular_progresso())

torneio.exibir_relatorio()