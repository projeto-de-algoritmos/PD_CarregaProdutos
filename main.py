itens = []
listaitens = []
def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 

    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] 
                          + K[i-1][w-wt[i-1]],   
                              K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
    
    print(K[n][W])
    return K

while(1):
    nomeproduto = str(input("digite o nome do produto.\n"))
    if nomeproduto == '':
        break
    valorproduto = int(input("digite o valor do produto.\n"))
    pesoproduto = int(input("digite o peso do produto.\n"))

    listaitens.append([nomeproduto,valorproduto,pesoproduto])

W = int(input("digite a capacidade de carregamento do.\n"))
# val = [60, 100, 120] 
# wt = [10, 20, 30] 
# W = 50
# listaitens = [['1',1,1],['2',2,2]]
val = []
wt = []

#print(listaitens)
for i in range(len(listaitens)):
    val.append(listaitens[i][1])
    wt.append(listaitens[i][2])

n = len(val)
# print(n)
# print(val)
# print(wt)
itens = knapSack(W, wt, val, n)
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