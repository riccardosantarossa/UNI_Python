
#IMPLEMENTAZIONE DI VARI ALGORITMI DI ORDINAMENTO

def letturaArray():
    tokens = input().split(" ")
    return [int(x) for x in tokens if x]  # "if x" is for filtering out empty tokens

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

def partition3vie(a, i, j):
    
    pivot = a[j-1]
    k = i
    h = i
    m = i
    
    while 0 <= k <= h <= m < j:
        
        if a[m] < pivot:
            if k < h < m:
                a[k], a[h], a[m] = a[m], a[k], a[h]
            elif k == h:
                a[k], a[m] = a[m], a[k]
            elif h == m:
                a[k], a[h] = a[h], a[k]
            k += 1
            h += 1
        elif a[m] == pivot:
            a[h], a[m] = a[m], a[h]
            h += 1
        m += 1
        
    return k, h

def quickSort(a, i=0, j=None):
    
    if j == None:
        j = len(a)
        
    #caso base
    if j - i <= 1:
        return
    
    #passo induttivo
    #k = partition(a, i, j)
    k = partition3vie(a, i, j)
    quickSort(a, i, k)
    quickSort(a, k + 1, j)


a = letturaArray()
b = quickSort(a)

print(b[a:len(a)])