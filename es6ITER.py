raw_input = input

#Implementare in l'algoritmo di ricerca dicotomica su array ordinati di interi.
#Il programma deve ricevere
#- un array ordinato di interi, rappresentato da una sequenza di numeri separati da spazi e terminata da "end of line",  
#- una chiave, rappresentata da un numero su una nuova riga
#e deve ritornare
#- la posizione della chiave nell'array, se esiste (0 = prima posizione)
#- oppure -1 se la chiave non e' presente nell'array
#La complessità asintotica dell'algoritmo dovrà essere O(log n).

# Lettura dell'array in input
def letturaArray():
    tokens = input().split(" ")
    return [int(x) for x in tokens if x]  # "if x" is for filtering out empty tokens

# Funzione di ricerca binaria iterativa
def IterBinarySearch(array, item):
    
    i = 0
    j = len(array) - 1
    k = int(item)
    
    while (i <= j):

        middle = i + (j - i) // 2

        if k == array[middle]:
            
            return middle
        
        elif array[middle] > k:
        
            j = middle - 1
        
        else:
            i = middle + 1

    return -1

a = letturaArray()
itemToFind = raw_input()
pos = IterBinarySearch(a, itemToFind)

print(pos)