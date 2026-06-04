class GaleriaAlienigena:
    def __init__(self, nome_galeria, obras):
        self.nome_galeria = nome_galeria
        self.obras = obras

    def adicionar_item(self, nome, valor):
        if nome != "":
            obra = {"nome": nome, "valor": valor}
            self.obras.append(obra)
            print("sua obra foi adcionada")
        else:
            print("nenhuma obra foi adicionada")

    def listar_itens(self):
        for obra in self.obras:
            print(f"Nome: {obra["nome"]} | Valor: {obra["valor"]}")

    def calcular_total(self):
        total = 0
        for obra in self.obras:
            total = total + obra["valor"]
        return total

    def encontrar_item_mais_valioso(self):
        mais_valioso = self.obras[0]

        for obra in self.obras:
            if obra["valor"] > mais_valioso["valor"]:
                mais_valioso = obra

        return mais_valioso

    def classificar_colecao(self):
        total = self.calcular_total()

        if total < 500:
            return "galeria comum"
        elif total <= 1500:
            return "galeria rara"
        elif total >= 1500:
            return "galeria intergaláctica"

    def exibir_relatorio(self):
        print("nome da galeria:", self.nome_galeria)
        print("total de raridade:", self.calcular_total())
        print("item mais valioso", self.encontrar_item_mais_valioso())
        print("Classificação:", self.classificar_colecao())


galeria = GaleriaAlienigena(
    "museu intergalatico",
    [
        {"nome": "quadro Nebular", "valor": 900},
        {"nome": "escultura Lunar", "valor": 400},
    ],
)

galeria.adicionar_item("lua sangrenta", 600)

galeria.listar_itens()

galeria.exibir_relatorio()