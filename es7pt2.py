from __future__ import print_function
raw_input = input

#PARTE 2

#Lettura dell'array in input
def letturaArray():
    tokens = raw_input().split(" ")
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
            
    

a = letturaArray()
b = letturaArray() 


#Creo l'array di intervalli da b
arrIntervalli = [(i, j) for (i,j) in zip(b[0::2], b[1::2])]


     