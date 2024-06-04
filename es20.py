
class Node:

    def __init__(self, data, value, index):

        self.key = data
        self.left = None
        self.right = None
        self.parent = None
        self.index = index
        self.value = value
    
    
class Tree:
    
    tree = [None]
    
    #inserimento del nodo al posto giusto
    def insertNode(self,t, k, v):
        
        node = Node(k, v , 0)
        
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
        
            self.tree.append(node)
            node.index = len(self.tree) - 1  
            

                
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
                return n.index
            elif key > n.key:
                t.find(t, n.right, key)
            else:
                t.find(t, n.left, key)
    
    
    #trova il minimo in un albero/sottoalbero        
    def searchMin(self, t):
        
        min = t[0]
        if min.left != None:
            if min.left.key < min.key:
                min = min.left
        
        return min
    
   
    #trova il successore del nodo con chiave richiesta
    
    
    #rimuove il nodo scelto dall'albero
    """def removeNode(self, t, key):
        
        rmIndex = t.find(t.tree[0], key).index
        rmNode = self.tree[rmIndex]
        
        if rmNode.left is None and rmNode.right is None:
            self.tree.pop(rmIndex)
        
        if rmNode.left is not None and rmNode.right is None:
            x = rmNode.parent
            rmNode.left.parent = x
        
        if rmNode.left is None and rmNode.right is not None:
            x = rmNode.parent 
            rmNode.right.parent = x
            
        if rmNode.left is not None and rmNode.right is not None:
            x = self.findIndex(self.findSuccessor(rmNode.key))"""
        
        
        
        

#MAIN

t = Tree()

while True:
    
    cmd = input()
    elts = cmd.split(" ")
    
    if elts[0] == "exit" :
        break
    
    #inserimento nell'albero
    elif elts[0] == "insert":
        k = int(elts[1])
        v = elts[2]
        t.insertNode(t,k,v)
    
    #calcolo della lunghezza   
    elif elts[0] == "show":
        print(t.show(t, t.tree[0]))
    
    #estrazione del minimo
    elif elts[0] == "remove":
        t.removeNode(t, t.tree[0], int(elts[1]))
       
    #estrazione del nodo radice
    elif elts[0] == "find":
        printIndex = t.find(t, t.tree[0], int(elts[1]))
        #print(t.tree[printIndex].value)
        print(printIndex)


    elif elts[0] == "clear":
        #t.clear(t)
        print(t.findIndex(t, elts[1]))