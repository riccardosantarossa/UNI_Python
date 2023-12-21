
class nodeWithIndex:
    
    def __init__(self, data, indice):
        
        self.data = data
        self.indice = indice


class auxHeap:
    
    n = nodeWithIndex(None, None)
    
    aux = []
    
    def length(self):
        
        return len(self.aux)
    
    #trovo il minimo della heap
    def getmin(self):
        
        assert len(self.aux) > 0, "Heap Vuota"
        return self.aux[0].data, self.aux[0].indice #il minimo di una aux sta in prima posizione
        
    #estraggo un elemento dalla heap
    def extract(self):
        
        self.aux[0] = self.aux.pop() #tolgo soltanto l'ultimo elemento dell'array, e me lo ritorna
        self.heapify(0)
    
    #inserisce un elemento nella heap portandolo nel posto giusto
    def insert(self, x):
        
        self.aux.append(x) #aggiungo in coda all'array
        self.moveUp(len(self.aux) - 1) #sposto il nuovo nodo dove effettivamente serve
        
    
    #costruisce la Heap dal vettore
    def buildHeap(self, a):
        
        self.aux = a.copy()
        
        for i in range (len(self.aux) -1, -1, -1):
            self.heapify(i)
            
            
    #modifico un elemento all'interno della heap   
    def change(self, i, x):
        
        assert i < len(self.aux), "errore nell'indice"
        
        if x < self.aux[i]:
            self.aux[i] = x
            self.moveUp(i)
        elif x > self.aux[i]:
            self.aux[i] = x
            self.heapify(i)
    
    #correzione della Heap VERSO IL BASSO
    def heapify(self, i):
        left = 2*i +1 
        right =  2*i +2
        
        argMin = i  #posizione dell'elemento corrente
        
        if left < len(self.aux) and self.aux[left] < self.aux[argMin]:
            argMin = left
        
        if right < len(self.aux) and self.aux[right] < self.aux[argMin]:
            argMin = right
            
        if i != argMin:
            self.aux[i], self.aux[argMin] = self.aux[argMin], self.aux[i]
            self.heapify(argMin)
    
    
    #sposta il nodo nel posto giusto all'interno della heap, VERSO L'ALTO
    def moveUp(self, i):
        
        if i == 0:
            return 
        
        parent = (i + 1) // 2 -1
        
        if self.aux[i] < self.aux[parent]:
            self.aux[i], self.aux[parent] = self.aux[parent], self.aux[i]
            
        self.moveUp(parent)
        


h = auxHeap()

a = {(3, 0), (2, 1), (1,2)}
h.buildHeap(a)
print(*h.aux)