
class nodeWithIndex:
    
    def __init__(self, data, index):
        
        self.data = data
        self.index = index


class auxHeap:
    
    aux = [nodeWithIndex(data=float('+inf'), index=0)] * 0
    
    def length(self):
        
        return len(self.aux)
    
    #trovo il minimo della heap
    def getmin(self):
        
        assert len(self.aux) > 0, "Heap Vuota"
        return self.aux[0].data, self.aux[0].index #il minimo di una aux sta in prima posizione
        
    #estraggo un elemento dalla heap
    def extract(self):
        
        self.aux.pop(0) #tolgo soltanto l'ultimo elemento dell'array, e me lo ritorna

        if len(self.aux) > 0:
            self.heapify(0)
    
    #inserisce un elemento nella heap portandolo nel posto giusto
    def insert(self, x, i):
        
        n = nodeWithIndex(data= x, index = i)
        
        self.aux.append(n) #aggiungo in coda all'array
        self.moveUp(len(self.aux) - 1) #sposto il nuovo nodo dove effettivamente serve
        
    
    #costruisce la Heap dal vettore
    def buildHeap(self, a):
        
        self.aux = a.copy()
        
        for i in range (len(self.aux) -1, -1, -1):
            self.heapify(i)
            
            
    #modifico un elemento all'interno della heap   
    def change(self, i, x):
        
        assert i < len(self.aux), "errore nell'index"
        
        if x[0] < self.aux[i]:
            self.aux[i][0] = x[0]
            self.moveUp(i)
        elif x[0] > self.aux[i][0]:
            self.aux[i][0] = x[0]
            self.heapify(i)
    
    #correzione della Heap VERSO IL BASSO
    def heapify(self, i):
        left = 2*i +1 
        right =  2*i +2
        
        argMin = i  #posizione dell'elemento corrente
        
        if left < len(self.aux) and self.aux[left][0] < self.aux[argMin][0]:
            argMin = left
        
        if right < len(self.aux) and self.aux[right][0] < self.aux[argMin][0]:
            argMin = right
            
        if i != argMin:
            self.aux[i][0], self.aux[argMin][0] = self.aux[argMin][0], self.aux[i][0]
            self.heapify(argMin)
    
    
    #sposta il nodo nel posto giusto all'interno della heap, VERSO L'ALTO
    def moveUp(self, i):
        
        if i == 0:
            return 
        
        parent = (i + 1) // 2 -1
        
        if self.aux[i].data < self.aux[parent].data:
            self.aux[i].data, self.aux[parent].data = self.aux[parent].data, self.aux[i].data
            
        self.moveUp(parent)
        
