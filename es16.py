
#Scrivere un programma che riceva in input un albero binario con nodi etichettati da chiavi di tipo numerico (interi) 
#e produca in output l'array corrispondente alla visita "in-order", ottenuta processando ricorsivamente l'albero bianario nel seguente ordine: 
#prima il sotto-albero del figlio sinistro, poi il nodo corrente ed infine il sotto-albero del figlio destro.

def letturaArray():
    tokens = input().split(" ")

    return [int(x) for x in tokens if x]  # "if x" is for filtering out empty tokens



def inOrder(a):
    
    