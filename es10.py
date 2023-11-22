
#Lettura dell'array in input
def letturaArray():
    tokens = input().split(" ")
    return [int(x) for x in tokens if x]  # "if x" is for filtering out empty tokens

def massimaDifferenza(a):
    
    #calcolo minimi per PREFISSI CRESCENTI
    minimi = [float('+inf')] * (len(a) + 1) #array che contiene n+1 volte infinito
    argMinimi = [None] * (len(a) + 1)

    for j in range (0, len(a)): #minimi[j] = min a[0...j-1]
        
        if a[j] < minimi[j] :
            minimi[j+1] = a[j]
            argMinimi[j+1] = j
        else:
            minimi[j+1] = minimi[j]
            argMinimi[j+1] = argMinimi[j] 

    #calcolo l'ESCURSIONE MASSIMA
    massimaDifferenza = float('-inf')
    argMassimaDifferenza = None

    for j in range(len(a)):
        
        diff = a[j] - minimi[j+1]
        if diff > massimaDifferenza:
            massimaDifferenza = diff
            argMassimaDifferenza = (argMinimi[j+1], j)
     
    return argMassimaDifferenza
   
a = letturaArray()
i, j = massimaDifferenza(a)
print(i,j)