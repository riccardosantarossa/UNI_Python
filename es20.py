
class Tree:

    def __init__(self, data, value):

        self.key = data
        self.left = None
        self.right = None
        self.parent = None
        self.value = value
    
    tree = [None]


    #inserimento del nodo al posto giusto
    def insertNode(self, k, v):
        node = Tree(k, v)
        
        x = self.tree[0]
        y = None

        while(x is not None):
            y = x
            if x.key > node.key:
                x = y.left
            else:
                x = y.right
        
        if y == None:
            self.tree[0] = node
        else:
            node.parent = y 
            if node.key < y.key:
                y.left = node
            else:
                y.right = node
        
            t.tree.append(node)

                
    #mostra l'albero in forma polacca
    def show(self, t, n):
        
        if n is None:
            return "NULL"
        else:
            return str(n.key) + ":" + n.value + " " + t.show(self, n.left) + " " +  t.show(self, n.right)
            
           
    #cancella l'albero
    def clear(self, t):
        t.tree = [None]
        
        
    #ricerca un nodo all'interno dell'albero
    def find(self, t, n, key):
        
        if n is None:
            print("Node not exists")
        else:
            if n.key == key:
                print(n.value)
            elif k > n.key:
                t.find(t, n.right, key)
            else:
                t.find(t, n.left, key)
            

    #rimuove il nodo scelto dall'albero
    def removeNode(self, t, key):
        
        treeCopy = t.tree.copy()
        t.clear(t)
        for x in treeCopy:
            if x.key != key:
                t.insertNode(x.key, x.value)

#MAIN

t = Tree(None, "")

while True:
    
    cmd = input()
    elts = cmd.split(" ")
    
    if elts[0] == "exit" :
        break
    
    #inserimento nell'albero
    elif elts[0] == "insert":
        k = int(elts[1])
        v = elts[2]
        t.insertNode(k,v)
    
    #calcolo della lunghezza   
    elif elts[0] == "show":
        print(t.show(t, t.tree[0]))
    
    #estrazione del minimo
    elif elts[0] == "remove":
        t.removeNode(t, int(elts[1]))
       
    #estrazione del nodo radice
    elif elts[0] == "find":
        t.find(t, t.tree[0], int(elts[1]))


    elif elts[0] == "clear":
        t.clear(t)
