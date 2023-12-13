
#Costruzione e gestione di MinHeap, devo implementare le operazioni di costruzione della heap, 
#calcolo della lunghezza della heap, ricerca del minimo della heap, con inserimento di un elemento
#ed estrazione del nodo radice, l'input dell'utente comprende anche i vari comandi come build,
#extract oppure o change


class MinHeap:
    
    minHeap = []
    
    def length(self):
        
        return len(self.minHeap)
    
    #trovo il minimo della heap
    def getmin(self):
        
        assert len(self.minHeap) > 0, "Heap Vuota"
        return self.minHeap[0] #il minimo di una MinHeap sta in prima posizione
        
    #estraggo un elemento dalla heap
    def extract(self):
        
        self.minHeap[0] = self.minHeap.pop() #tolgo soltanto l'ultimo elemento dell'array, e me lo ritorna
        self.heapify(0)
    
    #inserisce un elemento nella heap portandolo nel posto giusto
    def insert(self):
        
        self.minHeap.append() #aggiungo in coda all'array
        self.moveUp(len(self.minHeap) - 1) #sposto il nuovo nodo dove effettivamente serve
        
    
    #costruisce la Heap dal vettore
    def buildHeap(self, a):
        
        self.minHeap = a.copy()
        
        for i in range (len(self.minHeap) -1, -1, -1):
            self.heapify(i)
            
            
    #modifico un elemento all'interno della heap   
    def change(self, i, x):
        
        assert i < len(self.minHeap), "errore nell'indice"
        
        if x < self.minHeap[i]:
            self.minHeap[i] = x
            self.moveUp(i)
        elif x > self.minHeap[i]:
            self.minHeap[i] = x
            self.heapify(i)
    
    #correzione della Heap VERSO IL BASSO
    def heapify(self, i):
        left = 2*i +1 
        right =  2*i +2
        
        argMin = i  #posizione dell'elemento corrente
        
        if left < len(self.minHeap) and self.minHeap[left] < self.minHeap[argMin]:
            argMin = left
        
        if left < len(self.minHeap) and self.minHeap[right] < self.minHeap[argMin]:
            argMin = left
            
        if i != argMin:
            self.minHeap[i], self.minHeap[argMin] = self.minHeap[argMin], self.minHeap[i]
            self.heapify(argMin)
    
    
    #sposta il nodo nel posto giusto all'interno della heap, VERSO L'ALTO
    def moveUp(self, i):
        
        if i == 0:
            return 
        
        parent = (i + 1) // 2 -1
        
        if self.minHeap[i] < self.minHeap[parent]:
            self.minHeap[i], self.minHeap[parent] = self.minHeap[parent], self.minHeap[i]
            
        self.moveUp(parent)
        
        
h = MinHeap()

while True:
    
    cmd = input()
    elts = cmd.split(" ")
    
    if elts[0] == "exit" :
        break
    
    elif elts[0] == "build":
        a = [int(x) for x in elts[1:] if x]
        h.buildHeap(a)
        
    elif elts[0] == "length":
        print(h.length())
       
    elif elts[0] == "getmin":
        print(h.getmin())
               
    elif elts[0] == "extract":
        print(h.extract())
    
    elif elts[0] == "insert":
        el = int(elts[1])
        print(h.insert(el))
        
    elif elts[0] == "change":
        i = int(elts[1])
        x = int(elts[2])
        print(h.change(i, x))
        
    print(*h.minHeap)