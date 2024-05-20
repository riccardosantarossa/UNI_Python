class Tree:

    def _init_(self, data):

        self.key = data
        self.left = None
        self.right = None
        self.hr = 0
        self.hl = 0
    

def createTree(keys):

    if not keys:
        return None

    nodeKey = keys.pop()

    if nodeKey == "NULL":
        return None

    node = Tree(int(nodeKey))
    node.right = createTree(keys)
    node.left = createTree(keys)
    if node.right != None :
        node.hr = max(node.right.hr, node.right.hl)+1
    else :
        node.hr = 0

    if node.left != None :
        node.hl = max(node.left.hl, node.left.hr)+1
    else :
        node.hl = 0
   
    return node


def visitaInorder(root, res):

    if root:
        visitaInorder(root.left, res)
        res.append([root.key,root.hl,root.hr])
        #res.append(root.hl)
        #res.append(root.hr)
        visitaInorder(root.right, res)


def inOrder(v):

    treeNodes = v.split()
    treeNodes.reverse()
    root = createTree(treeNodes)
    res = []
    visitaInorder(root, res)
    res.reverse()
    return res

def isSort(a):
    for i in range(1, len(a)):
         if a[i][0] < a[i-1][0]:
            return 0
    return 1  

def isAvl(a):
    for i in range(1, len(a)):
         if not (abs(a[i][1] - a[i][2]) < 2):
            return 1
    return 2
    
def tester(a):
    if (isSort(a) == 1):
        return isAvl(a)
    else:
        return 0


#MAIN
a = input()
out = inOrder(a)
print(tester(out))
