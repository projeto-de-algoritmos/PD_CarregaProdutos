import knapSack
import carrinho

listaitens = []
itenscarregados = []
# listaitens = [['1',60,10],['2',100,20],['3',120,30]]
itens = []

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Cadastrar um produto")
    print("2. Ver quantidade maxima de centimetros cubicos carregados") 
    print("3. Ver Produtos do carrinho ") 
    print("4. Sair")
    print(67 * "-")


if __name__ == '__main__':
    loop=True
    
    while loop:
        print_menu()
        choice = input("Entre sua opcao [1-3]: ")            
        if choice=='1':
            print("Opcao 1 foi escolhida")
            nomeproduto = str(input("digite o nome do produto.\n"))
            valorproduto = int(input("digite o tamanho em centimetros cubicos do produto.\n"))
            pesoproduto = int(input("digite o peso em quilograma do produto.\n"))
            listaitens.append([nomeproduto,valorproduto,pesoproduto])
            # listaitens = [['1',60,10],['2',100,20],['3',120,30]]
        elif choice=='2':
            print("Opcao 2 foi escolhida")
            W = int(input("digite a capacidade em peso de carregamento do carrinho.\n"))
            n = len(listaitens)
            K = knapSack.main(W,listaitens, n) 
            itens = carrinho.main(K,n,listaitens, W)  
        elif choice=='3':
            print("Opcao 3 foi escolhida")
            for i in range(len(itens)):
                print()
                print(28 * "-" , 'produto '+str(i+1)+'.' , 28 * "-")
                print('nome do produto:' +str(itens[i][0]))
                print('tamanho do produto:' +str(itens[i][1]))
                print('peso do produto:' +str(itens[i][2]))
                print(56 * "-")
                print()
                
        elif choice=='4':
            print("Opcao 4 foi escolhida")
            print('Saindo....')
            loop=False
        else:
            input("Opcao incorreta. Aperte qualquer tecla para tentar novamente..")
