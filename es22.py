
class Node:

    def __init__(self, data, value, index):

        self.key = data
        self.left = None
        self.right = None
        self.parent = None
        self.index = index
        self.value = value
        self.height = 1

def rightRotate(xIndex):
    
    x = t[xIndex]
    y = t[x.left.index]
    
    if y.right is not None:
        z2 = t[y.right.index]
    else:
        z2 = None
 
    y.parent = x.parent

    if y.parent is not None:
        if x.key == y.parent.left.key:
            y.parent.left = y
        else:
            y.parent.right = y
    else:
        root[0] = y
        
    x.parent = y
    x.left = z2
    if z2 is not None:
        z2.parent = x
        x.height = z2.height + 1
    elif x.right is None:
        x.height = 1
    else:
        x.height = x.right.height + 1 
        
    y.right = x
    y.height = x.height + 1
    
    if root[0].key == y.key:
        root[0] = y

def leftRotate(xIndex):

    x = t[xIndex]
    y = t[x.right.index]
    
    if y.left is not None:
        z1 = t[y.left.index]
    else:
        z1 = None
 
    y.parent = x.parent

    if y.parent is not None:
        if x.key == y.parent.right.key:
            y.parent.right = y
        else:
            y.parent.left = y
    else:
        root[0] = y
        
    x.parent = y
    x.right = z1
    if z1 is not None:
        z1.parent = x
        x.height = z1.height + 1
    elif x.left is None:
        x.height = 1
    else:
        x.height = x.left.height + 1 
        
    y.left = x
    y.height = x.height + 1
    
    if root[0].key == y.key:
        root[0] = y
 
def fixHeightUpwInsert(nIndex):
    
    n = t[nIndex]
    if n.parent is None:
        par = None
    else:
        par = t[n.parent.index] 

    #risalgo l'albero modificando le altezze necessarie 
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
    fixHeightUpwInsert(node.index)    
        
       
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
    
def fixHeightUpwRemove(nIndex):
    
    n = t[nIndex]
    if n.right is None and n.left is None:
        n.height = 1
    elif n.left is None:
        n.height = n.right.height + 1
    elif n.right is None:
        n.height = n.left.height + 1
    else:
        n.height = max(n.left.height, n.right.height) + 1

    if n.parent is None:
        par = None
    else:
        par = t[n.parent.index] 

    #risalgo l'albero modificando le altezze necessarie - bigO(n)
    while par is not None:
        if par.left is not None and par.left.key == n.key:
            #n è figlio sinistro
            if par.right is not None:
                if par.right.height > n.height:
                    break
                else:
                    par.height = max(n.height, par.right.height) + 1
            
            else:
                #n è l'unico figlio (sinistro)
                par.height = n.height + 1
        else:
            #n è figlio destro
            if par.left is not None:
                if par.left.height > n.height:
                    break
                else:
                    par.height = max(par.left.height, n.height) + 1

            else:
                #n è l'unico figlio (destro)
                par.height = n.height + 1
        
        n = par
        if par.parent is None:
            par = None
        else:
            par = t[par.parent.index]
            
            
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

        pNode = t[x.parent.index]
        
        if x.parent.left is not None:
            if x.key == x.parent.left.key:
                pNode.left = v

            else:
                pNode.right = v
        else:
            pNode.right = v

        fixHeightUpwRemove(pNode.index)

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
 
    elif elts[0] == "clear":
        t = []
        root = [None]
        