
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



    def showTree(self, t):
        for x in t:
            print(str(x.key)+ ":" + x.value)
            


#MAIN

t = Tree(None, "")

while True:
    
    cmd = input()
    elts = cmd.split(" ")
    
    if elts[0] == "exit" :
        break
    
    #inserimento nell'albero'
    elif elts[0] == "insert":
        k = int(elts[1])
        v = elts[2]
        t.insertNode(k,v)
    
    #calcolo della lunghezza   
    elif elts[0] == "show":
        t.showTree(t.tree)
    
    #estrazione del minimo
    elif elts[0] == "remove":
        print("")
    
    #estrazione del nodo radice
    elif elts[0] == "find":
        print("")


    elif elts[0] == "clear":
        print("")
