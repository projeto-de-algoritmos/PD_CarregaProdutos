def main(K,n, listaitens, W):
    itensescolhidos = []
    aux = W
    carrinho = False    
    for linha in range(n):
        if(K[linha][aux] != K[linha-1][aux]):
            carrinho = True
        
        if carrinho:
            itensescolhidos.append(listaitens[linha-1])
            peso = listaitens[linha-1][2]
            aux -= peso
            
    return itensescolhidos