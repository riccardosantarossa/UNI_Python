
#Scrivere un programma che riceva in input un albero binario con nodi etichettati da chiavi di tipo numerico (interi) 
#e produca in output l'array corrispondente alla visita "in-order", ottenuta processando ricorsivamente l'albero bianario nel seguente ordine: 
#prima il sotto-albero del figlio sinistro, poi il nodo corrente ed infine il sotto-albero del figlio destro.

class Tree:
    
    #definizione dell'oggetto nodo
    def __init__(self, data):
        
        self.key = data
        self.left = None
        self.right = None


def createTree(keys):
    
    if not keys:
        return None
    
    nodeKey = keys.pop()
    
    if nodeKey == "NULL":
        return None
    
    node = Tree(int(nodeKey))
    node.right = createTree(keys)
    node.left = createTree(keys)
    
    return node
    
    
def visitaInorder(root, res):
    
    if root:
        visitaInorder(root.left, res)
        res.append(root.key)
        visitaInorder(root.right, res)
        

def inOrder(v):
    
    treeNodes = v.split()
    treeNodes.reverse()
    root = createTree(treeNodes)
    res = []
    visitaInorder(root, res)
    return res[::-1]

#MAIN
a = input()
out = inOrder(a)
print(*out)


