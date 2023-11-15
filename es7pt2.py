from __future__ import print_function

#PARTE 2

#Lettura dell'array in input
def letturaArray():
    tokens = input().split(" ")
    return [int(x) for x in tokens if x]  # "if x" is for filtering out empty tokens


#Creo il tipo base della struttura SEGMENT TREE
class SegmentNode:
    
    #variabili
    low = None
    high = None
    massimo = None
    left = None    #figlio sinistro
    right = None   #figlio destro

    #costruttore
    def __init__(self, a, low, high):
        assert high - low > 0
        self.low = low
        self,high = high
        
        #caso base -> foglia
        if high-low == 1:
            self.massimo = a[low]
            self.left = None
            self.right = None
        else:
            mid = (low + high) //2
            self.left = SegmentNode(a,low, mid)
            self.right = SegmentNode(a,mid, high)
            self.massimo = max(self.left.massimo, self.right.massimo)
     
     
def query(i, j, s):
    
    assert s != None
    assert s.low <= i < j <= s.high
    
    #caso fortunato i, j = low, high
    if s.low == i and s.high == j:  
        return s.massimo
    
    #caso in cui high-low > j-i quindi s.lef,s.right !=
    assert s.left != None and s.right != None
    assert s.left.high == s.right.low 
    mid = s.left.high
    
    #caso in cui mid cade fuori e a sinistra di i,j
    if  mid <= i: 
        return query(i, j, s.right)
    elif j <= mid:
        return query(i, j, s.left)
    else: 
         assert i <mid <= j  
         return max(query(i, mid, s.left), query(i, mid, s.right))
     


a = letturaArray()
b = letturaArray() 

c = [(i, j) for (i,j) in zip(b[0::2], b[1::2])]
s= SegmentNode(a, 0, len(a))

for (i,j) in c: print(query(1,7,s))



     