
#Calcolare il k-esimo elemento più piccolo in un array dato. 
#Il programma deve ricevere in input una sequenza di interi separati da spazio e, su una nuova riga, un ulteriore intero positivo k
# e deve produrre in output il k-esimo elemento più piccolo, ovvero il k-esimo elemento dell'array qualora quest'ultimo fosse ordinato.

def letturaArray():
    tokens = input().split(" ")
    return [int(x) for x in tokens if x]  # "if x" is for filtering out empty tokens


#PARTE 1: QUICK SELECT

def partition(a, i, j):
        
    pivot = a[j-1]
    k = i
    h = i
    
    while 0 <= k <= h < j:
        
        if a[h] <= pivot:
            a[k], a[h] = a[h], a[k]
            k += 1
        
        h += 1
        
    return k-1

def quickSort(a, i=0, j=None):
    
    if j == None:
        j = len(a)
        
    #caso base
    if j - i <= 1:
        return
    
    #passo induttivo
    #k = partition(a, i, j)
    k = partition(a, i, j)
    quickSort(a, i, k)
    quickSort(a, k + 1, j)

    return a

def quickSelect(a, h, i=0, j=None):
    
    if j == None:
        j = len(a)
        
    #h compreso tra i incluso e j escluso
    #CASO BASE
    if j-i == 1 and h == i:
        return a[i]
    elif i == j: 
        return None
    
    k = partition(a, i, j)
    
    #PASSO INDUTTIVO
    if i <= h < k:
        return quickSelect(a, h, i, k)
    elif k <= h < j:
        return quickSelect(a, h, k, j) 


#a = letturaArray()
#h = int(input()) -1
#print(quickSelect(a, h))


#-------------------------------------------------------------------------------------------------------------------

#PARTE 2: HEAP SELECT

from standardHeap import * 
from auxHeap import * 

def heapSelect(a, k):
    h = MinHeap()
    h2 = auxHeap()

    h = h.buildHeap(a)
    h2.insert(h.minHeap[0], 0)

    for i in range(0, int(k)):
        
        (x, y) = h2.getmin()
        
        h2.extract()
        
        l = 2*y + 1
        r = 2*y + 2
        
        if l != None and l < h.length():
            h2.insert(h.minHeap[l], l)
            
        if r != None and r < h.length():
            h2.insert(h.minHeap[r], r)
        
    (xmin, indmin) = h2.getmin()

    return (xmin)

a = letturaArray()
k = int(input()) -1
print(heapSelect(a, k))