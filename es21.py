#da implementare con remove-height
class Node:

    def __init__(self, data, value, index):

        self.key = data
        self.left = None
        self.right = None
        self.parent = None
        self.index = index
        self.value = value
        self.height = 1
    
def FixHeightUpwInsert(nIndex):
    n = t[nIndex]
    if n.parent is None:
        par = None
    else:
        par = t[n.parent.index] 

    #risalgo l'albero modificando le altezze necessarie - bigO(logn)
    while par is not None:
        if par.left is not None and par.left.key == n.key:
            #n è figlio sinistro
            if par.right is not None:
                if par.right.height < n.height:
                    par.height = par.height + 1
                else:
                    break
            
            else:
                #n è l'unico figlio (sinistro)
                par.height = par.height + 1
        else:
            #n è figlio destro
            if par.left is not None:
                if par.left.height < n.height:
                    par.height = par.height + 1
                else:
                    break

            else:
                #n è l'unico figlio (destro)
                par.height = par.height + 1
        
        n = par
        if par.parent is None:
            par = None
        else:
            par = t[par.parent.index]
        

 
#inserimento del nodo al posto giusto
def insertNode(t, root, k, v):
    
    node = Node(k, v , len(t))
    
    x = root[0]
    y = None

    while(x is not None):
        y = x
        if x.key > node.key:
            x = y.left
        else:
            x = y.right
    
    if y == None:
        root[0] = node
    else:
        node.parent = y 
        if node.key < y.key:
            y.left = node
        else:
            y.right = node
    
    t.append(node)
    FixHeightUpwInsert(node.index)    
        
       
#mostra l'albero in forma polacca
def show(t, n):
    
    if n is None:
        return "NULL"
    else:
        return str(n.key) + ":" + n.value + ":" + str(n.height) + " " + show(t, n.left) + " " + show(t, n.right)
        
            
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


#trova il successore del nodo con chiave richiesta
def findSuccessor(t, root, key):
    
    xIndex = find(t, root[0], key)
    x = t[xIndex]
    
    x = x.right
    
    while x.left is not None:
        x = x.left
    
    return x.index
    

#rimuove il nodo scelto dall'albero
def removeNode(t, root, key):
    
    rmIndex = find(t, root[0], key)
    z = t[rmIndex]
    
    if z.left is None or z.right is None:
        x = z
    else:
        rmIndex = findSuccessor(t, root, z.key)
        x = t[rmIndex]
        
    if x.left is not None:
        v = x.left
    else:
        v = x.right
    
    if v is not None:
        
        vIndex = find(t, root[0], v.key)
        v = t[vIndex]
        v.parent = x.parent
    
    if x.parent is not None:
        
        pIndex = find(t, root[0], x.parent.key)
        pNode = t[pIndex]
        
        if x.parent.left is not None:
            if x.key == x.parent.left.key:
                pNode.left = v
            else:
                pNode.right = v
        else:
            pNode.right = v
    else:
        root[0] = v
        
    if x.index != z.index:
        z.key = x.key
        z.value = x.value
   
    
#MAIN

root = [None]
t = []

while True:
    
    cmd = input()
    elts = cmd.split(" ")
    
    if elts[0] == "exit" :
        break
    
    #inserimento nell'albero
    elif elts[0] == "insert":
        k = int(elts[1])
        v = elts[2]
        insertNode(t,root,k,v)
    
    #calcolo della lunghezza   
    elif elts[0] == "show":
        print(show(t, root[0]))
    
    #estrazione del minimo
    elif elts[0] == "remove":
        removeNode(t, root, int(elts[1]))
       
    #estrazione del nodo radice
    elif elts[0] == "find":
        printIndex = find(t, root[0], int(elts[1]))
        print(t[printIndex].value)

    #altezza dell'albero T
    elif elts[0] == "height":
        if root[0] is None:
            print("0")
        else:
            print(root[0].height)
 
    elif elts[0] == "clear":
        t = []
        root = [None]
        