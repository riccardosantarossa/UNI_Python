
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
        if y.parent.left is not None and x.key == y.parent.left.key:
            y.parent.left = y
        else:
            y.parent.right = y
    else:
        root[0] = y
        
    x.parent = y
    x.left = z2
    if z2 is not None:
        z2.parent = x
        if x.right is not None:
            x.height = max(z2.height, x.right.height) + 1
        else:    
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

    if y.parent is not None :
        if y.parent.right is not None and x.key == y.parent.right.key:
            y.parent.right = y
        else:
            y.parent.left = y
    else:
        root[0] = y
        
    x.parent = y
    x.right = z1
    if z1 is not None:
        z1.parent = x
        if x.left is not None:
            x.height = max(z1.height, x.left.height) + 1
        else:
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
                if n.height - par.right.height == 2:
                    #rotazione a destra su parent, richiede controllo dei ripoti
                    if n.left is not None:
                        lhn = n.left.height
                    else:
                        lhn = 0
                    if n.right is not None:
                        rhn = n.right.height
                    else:
                        rhn = 0
                    
                    if lhn >= rhn:
                        rightRotate(par.index)
                    else:
                        leftRotate(n.index)
                        rightRotate(par.index)
                elif n.height - par.right.height == 1:
                    par.height = n.height + 1
                else:
                    break
            
            else:
                #n è l'unico figlio (sinistro)
                if n.height == 2:
                    #rotazione a destra su parent, richiede controllo dei ripoti
                    if n.left is not None:
                        lhn = n.left.height
                    else:
                        lhn = 0
                    if n.right is not None:
                        rhn = n.right.height
                    else:
                        rhn = 0
                    
                    if lhn >= rhn:
                        rightRotate(par.index)
                    else:
                        leftRotate(n.index)
                        rightRotate(par.index)
                else:
                    par.height = par.height + 1
        
        else:
            
            #n è figlio destro
            if par.left is not None:
                if n.height - par.left.height == 2:
                    #rotazione a sinistra su parent, richiede controllo dei ripoti
                    if n.left is not None:
                        lhn = n.left.height
                    else:
                        lhn = 0
                    if n.right is not None:
                        rhn = n.right.height
                    else:
                        rhn = 0
                    
                    if lhn > rhn:
                        rightRotate(n.index)
                        leftRotate(par.index)
                    else:
                        leftRotate(par.index)
                elif n.height - par.left.height == 1:
                    par.height = n.height + 1
                else:
                    break

            else:
                #n è l'unico figlio (destro)
                if n.height == 2:
                    #rotazione a sinistra su parent, richiede controllo dei ripoti
                    if n.left is not None:
                        lhn = n.left.height
                    else:
                        lhn = 0
                    if n.right is not None:
                        rhn = n.right.height
                    else:
                        rhn = 0
                    
                    if lhn > rhn:
                        rightRotate(n.index)
                        leftRotate(par.index)
                    else:
                        leftRotate(par.index)
                else:
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
    
def fixHeightUpwRemove(nIndex, pIndex):
    if nIndex == -1:
        # n è None
        par = t[pIndex]
        if par.left is not None:
            # par ha figlio sx, n era destro ed è stato rimosso
            if par.left.height == 2:
                if par.left.left is not None:
                    lh = 1
                else:
                    lh = 0
                if par.left.right is not None:
                    rh = 1
                else:
                    rh = 0
                if lh >= rh:
                    rightRotate(pIndex)
                else:
                    leftRotate(par.left.index)
                    rightRotate(pIndex)

        elif par.right is not None:
            # par ha figlio dx, n era sinistro ed è stato rimosso
            if par.right.height == 2:
                if par.right.left is not None:
                    lh = 1
                else:
                    lh = 0
                if par.right.right is not None:
                    rh = 1
                else:
                    rh = 0
                if lh > rh:
                    rightRotate(par.right.index)
                    leftRotate(pIndex)
                else:
                    leftRotate(pIndex)
        else:
            par.height = 1
        
        n = par
        if par.parent is not None:
            par = t[par.parent.index]
        else:
            par = None

    else:
        n = t[nIndex]
        par = t[pIndex] 

        #risalgo l'albero modificando le altezze necessarie 
    while par is not None:
        if par.left is not None and par.left.key == n.key:
                
            #n è figlio sinistro
            if par.right is not None:
                if par.right.height - n.height == 2:
                    #rotazione a sinistra su parent, richiede controllo dei ripoti
                    if par.right.left is not None:
                        lhn = par.right.left.height
                    else:
                        lhn = 0
                    if par.right.right is not None:
                        rhn = par.right.right.height
                    else:
                        rhn = 0
                        
                    if lhn > rhn:
                        rightRotate(par.right.index)
                        leftRotate(par.index)
                    else:
                        leftRotate(par.index)
                elif par.right.height - n.height == 1:
                    par.height = max(par.right.height, n.height)  + 1
                else:
                    par.height = max(par.right.height, n.height)  + 1
                
            else:
                    #n è l'unico figlio (sinistro)
                par.height = n.height + 1
            
        else:
            
            #n è figlio destro
            if par.left is not None:
                if par.left.height - n.height == 2:
                        #rotazione a destra su parent, richiede controllo dei ripoti
                    if par.left.left is not None:
                        lhn = par.left.left.height
                    else:
                        lhn = 0
                    if par.left.right is not None:
                        rhn = par.left.right.height
                    else:
                        rhn = 0
                        
                    if lhn >= rhn:
                        rightRotate(par.index)
                    else:
                        leftRotate(par.left.index)
                        rightRotate(par.index)
                elif par.left.height - n.height == 1:
                    par.height = max(par.left.height, n.height) + 1
                else:
                    par.height = max(par.left.height, n.height) + 1
                
            else:
                    #n è l'unico figlio 
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
        if v is None:
            vIndex = -1
        else:
            vIndex = v.index
        fixHeightUpwRemove(vIndex, pNode.index)

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
        