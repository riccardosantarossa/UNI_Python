raw_input = input

#PARTE 1

#Lettura dell'array in input
def letturaArray():
    tokens = raw_input().split(" ")
    return [int(x) for x in tokens if x]  # "if x" is for filtering out empty tokens

#Fa la somma di un determinato intervallo, complessità QUADRATICA
def sommaIntervallo(a, i, j):
    s = 0
    for k in range(i, j+1):
        s = s + a[k]
    return s

#Funzione che usa una struttura ausiliaria
def sommaAusiliaria(a):
    aux = [0] * (len(a)+1)
    for i in range(i, j+1):
        aux[i+1] = aux[i] + a[i]
    return aux

#Funzione somma con complessità LINEARE
def sommaOttimizzata(a, i, j, aux):
    return  

arr = letturaArray()
b = letturaArray() 

#Creo l'array di intervalli da b
arrIntervalli = [(i, j) for (i,j) in zip(b[0::2], b[1::2])]

#Funzione vera e propria
for (i, j) in arrIntervalli:
        print(sommaIntervallo(arr,i, j), end=' ')