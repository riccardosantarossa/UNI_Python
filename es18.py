
#Scrivere un programma che riceva in input un albero binario in cui ogni nodo è etichettato da un intero (denominato chiave) 
#e decida se questo sia o meno un albero binario di ricerca, vale a dire soddisfi o meno la seguente proprietà: 
#se x è un nodo dell'albero e y è un suo discendente nel sotto-albero di sinistra (rispettivamente, di destra)
#allora la chiave di x deve essere strettamente maggiore (rispettivamente, minore) di quella di y
#In particolare, in un albero binario di ricerca i nodi hanno sempre chiavi distinte. 


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
    return res


#Se la visita IN ORDER di un albero è effettivamente ordinata, allora è un BST
def checkBST(t):

    for i in range(1, len(t)): 

        if t[i] < t[i-1]:
            return 0

    return 1


a = input()
#Faccio la INORDER
binaryTree = inOrder(a)
tryBST = binaryTree.copy()
#Inverto l'ordine
tryBST.reverse()
#Controllo
print(checkBST(tryBST))