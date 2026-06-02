capsula=0
ano=0
capsula=int(input("Em qual ano a capsula do tempo pode ser aberta? "))
mensagem=input("qual a sua mensagem?")
ano=int(input("Qual ano estamos? "))
if ano>capsula:
    print("capsula do tempo aberta")
    print(mensagem)
else:
    quantidade=capsula-ano
    print (f"ainda falta {quantidade} ano para abrir a capsula do tempo")
