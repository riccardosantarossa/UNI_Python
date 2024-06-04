
class Node:

    def __init__(self, data, value, index):

        self.key = data
        self.left = None
        self.right = None
        self.parent = None
        self.index = index
        self.value = value
    
    
#inserimento del nodo al posto giusto
def insertNode(t, k, v):
    
    node = Node(k, v , 0)
    
    x = t[0]
    y = None

    while(x is not None):
        y = x
        if x.key > node.key:
            x = y.left
        else:
            x = y.right
    
    if y == None:
        t[0] = node
    else:
        node.parent = y 
        if node.key < y.key:
            y.left = node
        else:
            y.right = node
    
        t.append(node)
        node.index = len(t) - 1  
        

            
#mostra l'albero in forma polacca
def show(t, n):
    
    if n is None:
        return "NULL"
    else:
        return str(n.key) + ":" + n.value + " " + show(t, n.left) + " " + show(t, n.right)
        
            
#ricerca un nodo all'interno dell'albero
def find(t, n, key):
    
    if n is None:
        print("Node not exists")
    else:
        if n.key == key:
            return n.index
        elif key > n.key:
            return find(t, n.right, key)
        else:
            return find(t, n.left, key)


#trova il minimo in un albero/sottoalbero        
def searchMin(t, n):
    
    min = n
    if min.left != None:
        if min.left.key < min.key:
            min = min.left
    
    return min.key


#trova il successore del nodo con chiave richiesta
def findSuccessor(t, key):
    
    xIndex = find(t, t[0], key)
    x = t[xIndex]
    
    if x.right is not None:
        return searchMin(t, x.right)
    else:
        succ = x.parent
        while succ is not None and x.key == succ.right.key:
            x = succ
            succ = x.parent
        
        return succ

#rimuove il nodo scelto dall'albero
def removeNode(t, key):
    
    rmIndex = find(t, t[0], key)
    rmNode = t[rmIndex]
    
    if rmNode.left is None or rmNode.right is None:
        x = rmNode
    else:
        x = findSuccessor(t, rmNode.key)
        
    if x.left is not None:
        v = x.left
    else:
        v = x.right
    
    if v is not None:
        v.parent = x.parent
    
    if x.parent is not None:
        if x.key == x.parent.left.key:
            x.parent.left = v
        else:
            x.parent.right = v
    else:
        t[0] = v
        
    if x.key != key:
        key = x.key
   
    t.pop(rmIndex)
    
#MAIN

t = [None]

while True:
    
    cmd = input()
    elts = cmd.split(" ")
    
    if elts[0] == "exit" :
        break
    
    #inserimento nell'albero
    elif elts[0] == "insert":
        k = int(elts[1])
        v = elts[2]
        insertNode(t,k,v)
    
    #calcolo della lunghezza   
    elif elts[0] == "show":
        print(show(t, t[0]))
    
    #estrazione del minimo
    elif elts[0] == "remove":
        removeNode(t, int(elts[1]))
       
    #estrazione del nodo radice
    elif elts[0] == "find":
        printIndex = find(t, t[0], int(elts[1]))
        print(t[printIndex].value)


    elif elts[0] == "clear":
        t = [None]
        