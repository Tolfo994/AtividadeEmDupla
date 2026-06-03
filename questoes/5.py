class CofreDoDragao:
    def __init__(self, nome_dragao, tesouros):
        self.nome_dragao = nome_dragao
        self.tesouros = tesouros
        
    def adicionar_item(self, nome, valor):
        if nome == "":
            print("não pode estar escrito nada")
        elif valor <= 0:
            print("o valor do tesou tem que ser maior que 0")
        else:
            self.tesouros.append(f"nome: {nome}, valor: {valor}")
            
    def listar_itens(self):
        if len(self.tesouros) == 0:
            print("o cofre esta vazio")
        else:
            print("os tesouros são:")
            for tesouro in self.tesouros:
                partes = tesouro.split(",")
                nome = partes[0].split(":")[1].strip()
                valor = partes[1].split(":")[1].strip()
                print(f"- {nome}: {valor}")
                
    def calcular_total(self):
        total = 0
        for tesouro in self.tesouros:
            valor_str = tesouro.split(",")[1].split(":")[1].strip()
            total += int(valor_str)
        return total
        
    def encontrar_item_mais_valioso(self):
        if len(self.tesouros) == 0:
            return "nenhum tesouro no cofre"
            
        mais_valioso = self.tesouros[0]
        for tesouro in self.tesouros:
            valor_atual = int(tesouro.split(",")[1].split(":")[1].strip())
            valor_maximo = int(mais_valioso.split(",")[1].split(":")[1].strip())
            
            if valor_atual > valor_maximo:
                mais_valioso = tesouro
                
        nome = mais_valioso.split(",")[0].split(":")[1].strip()
        valor = mais_valioso.split(",")[1].split(":")[1].strip()
        return f"{nome}( valor {valor})"
        
    def classificar_colecao(self):
        total = self.calcular_total()
        if total < 500:
            return "coleção pequena"
        elif total <= 1500:
            return "coleção respeitavel"
        else:
            return "coleção lendaria"
            
    def exibir_relatorio(self):
        print(f"dragão: {self.nome_dragao} ")
        print(f"total acumulado: {self.calcular_total()}")
        print(f"item mais valioso: {self.encontrar_item_mais_valioso()}")
        print(f"calssificação: {self.classificar_colecao()}")
        self.listar_itens()

cofre = CofreDoDragao("guster", [])
cofre.adicionar_item("trofeu", 500)
print()
cofre.exibir_relatorio()
