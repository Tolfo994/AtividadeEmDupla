class ExpedicaoTemplo:
    def __init__(self, nome_expedicao, desafios, energia_inicial):
        self.nome_expedicao = nome_expedicao
        self.desafios = desafios
        self.energia = energia_inicial
        self.pontos = 0
        self.desafios_concluidos = []
    def listar_desafios(self):
        for i, desafio in enumerate(self.desafios):
            print(i, "-", desafio["nome"], "-", desafio["custo"], "-", desafio["pontuacao"])
    def tentar_desafio(self, numero_desafio):
        if numero_desafio < 0 or numero_desafio >= len(self.desafios):
            print("desafio invalido")
            return
        desafio = self.desafios[numero_desafio]
        if desafio["nome"] in self.desafios_concluidos:
            print("desafio ja concluido")
        elif self.energia >= desafio["custo"]:
            self.energia -= desafio["custo"]
            self.pontos += desafio["pontuacao"]
            self.desafios_concluidos.append(desafio["nome"])
            print("desafio concluido")
        else:
            print("energia insuficiente")
    def calcular_progresso(self):
        return len(self.desafios_concluidos)
    def verificar_situacao(self):
        if len(self.desafios_concluidos) == len(self.desafios):
            return "expedicao concluida"
        elif self.energia == 0:
            return "expedicao encerrada sem energia"
        else:
            return "expedicao em andamento"
    def exibir_relatorio(self):
        print("expedicao:", self.nome_expedicao)
        print("energia:", self.energia)
        print("pontos:", self.pontos)
        print("concluidos:", self.desafios_concluidos)
        print("situacao:", self.verificar_situacao())
desafios = [
    {"nome": "ponte quebrada", "custo": 20, "pontuacao": 30},
    {"nome": "porta secreta", "custo": 15, "pontuacao": 25}
]
expedicao = ExpedicaoTemplo("templo antigo", desafios, 50)
expedicao.listar_desafios()
expedicao.tentar_desafio(0)
expedicao.tentar_desafio(1)
expedicao.exibir_relatorio()