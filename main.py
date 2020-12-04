import knapSack

listaitens = []
itenscarregados = []


while(1):
    nomeproduto = str(input("digite o nome do produto.\n"))
    if nomeproduto == '':
        break
    valorproduto = int(input("digite o valor do produto.\n"))
    pesoproduto = int(input("digite o peso do produto.\n"))

    listaitens.append([nomeproduto,valorproduto,pesoproduto])

# listaitens = [['1',60,10],['2',100,20],['3',120,30]]
W = int(input("digite a capacidade de carregamento do.\n"))

n = len(listaitens)

maximo = knapSack.main(W,listaitens, n)
print(maximo)

# itensLevados = []
# estahNoCaminhao = False
# for linha in range(len(val), 0, -1):
#         if(itens[linha][W] != itens[linha-1][W]):
#             estahNoCaminhao = True
        
#         if estahNoCaminhao:
#             wt = val[linha-1]
#             itensLevados.append(val[linha-1])
#             W -= wt

##print(itensLevados)