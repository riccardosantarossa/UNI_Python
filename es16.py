
#Scrivere un programma che riceva in input un albero binario con nodi etichettati da chiavi di tipo numerico (interi) 
#e produca in output l'array corrispondente alla visita "in-order", ottenuta processando ricorsivamente l'albero bianario nel seguente ordine: 
#prima il sotto-albero del figlio sinistro, poi il nodo corrente ed infine il sotto-albero del figlio destro.

def letturaArray():
    tokens = input().split(" ")
    return [x for x in tokens]  # "if x" is for filtering out empty tokens


def left(i):
    return  2*i + 1 

def right(i):
    return  2*i + 2
    

def inOrder(a, x = None):
    
    if x == None:
        x = 0
    
    r = right(x)
    l = left(x)
        
    if a[x] != 'NULL' and r < len(a):
        
        inOrder(a, l)
        print(a[x])
        inOrder(a, r)
    
        

            
        
a = letturaArray()
inOrder(a)