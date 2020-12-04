def main(W, listaitens, n): 
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 

    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif listaitens[i-1][2] <= w: 
                K[i][w] = max(listaitens[i-1][1] 
                          + K[i-1][w-listaitens[i-1][2]],   
                              K[i-1][w])
                ## print(w)
                # if(w < W):
                #     # print(w,W)
                #     itenscarregados.append(listaitens[i-1])
                # else:
                #     for k in range(itenscarregados): 
                #         itenscarregados[k] = []
            else: 
                K[i][w] = K[i-1][w] 
    
    #print(K[n][W])
    # print(itenscarregados)
    return K[n][W]