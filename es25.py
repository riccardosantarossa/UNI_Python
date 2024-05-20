
#Si richiede di implementare un algoritmo polinomiale per calcolare la distanza di editing (nota anche come distanza di Levenshtein) fra due stringhe fornite in input.
#Date due stringhe x e y, la distanza di editing fra xe y è definita come il numero minimo di modifiche elementari (inserimento, cancellazione, o   editituzione di un carattere) 
#che consentono di trasformare xin y.
#Ad esempio, la distanza di editing fra "bar" e "biro" è 2: per trasformare "bar" in "biro" è sufficiente   editituire l'occorrenza del carattere "a" con il carattere "i" e 
#inserire il carattere "o" alla fine.
#L'algoritmo che calcola la distanza di editing fra due stringhe x e y date dovrà prendere tempo al più quadratico nelle lunghezze di x e y, precisamente tempo O(|x|⋅|y|)
#Il programma che implementa tale algoritmo dovrà ricevere le stringhe x e y su due righe di input (è anche possibile assumere che le stringhe non contengano spazi) 
#e dovrà stampare in output il valore della distanza di editing.

#import numpy as np

def editingDistance(x, y):
    
    righeMatrice = len(x) + 1
    colonneMatrice = len(y) + 1
    
    matrice = [([0] * colonneMatrice) for i in range(righeMatrice)]
    #matrice = np.zeros((righeMatrice, colonneMatrice))
    
    for i in range(righeMatrice):
        matrice[i][0] = i
        
    for j in range(colonneMatrice):
        matrice[0][j] = j
        
        
    for i in range(1, righeMatrice):
        for j in range(1, colonneMatrice):
            
            #verifico se devo modificare la lettera o meno
            if(x[i-1] == y[j-1]):
                edit = 0
            else:
                edit = 1
            
            matrice[i][j] = min(matrice[i-1][j] + 1, matrice[i][j-1] + 1, matrice[i-1][j-1] + edit)
            
    return matrice[i][j]


#main
stringa1 = input()
stringa2 = input()

print(int(editingDistance(stringa1, stringa2)))