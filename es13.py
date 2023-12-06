
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

    return a

#-------------------------------------------------------------------

def insertionSort(a):
    
    for i in range (1, len(a)):
        
        k = a[i]
        j = i-1
        
        while j >= 0 and a[j] > k:
            
            a[j+1] = a[j]
            j -= 1
            
        a[j+1] = k
        
    return a

#-------------------------------------------------------------------
 
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    
    return arr

def mergeSort(a, p = 0, q = None):
    
    if q == None:
        q = len(a)
    
    if p < q :
        
        r = (p + q) // 2
        mergeSort(a, p, r)
        mergeSort(a, r+1, q)
        a = merge(a, p, r, q)
        
    return a

#-------------------------------------------------------------------

def right(i):
    return 2*i +1

def left(i):    
    return 2*i

def parent(i):
    return i/2 

def heapify(h, i):
    
    l = left(i)
    r = right(i)
    
    if l <= len(h) and h[l] > h[i]:
        m = l
    else:
        m = i
        
    if r <= len(h) and h[r] > h[m]:
        m = r
        
    if i != m:
        h[i], h[m] = h[m], h[i]
        heapify(h,m)
    
    return h

def buildHeap(a):
    
    for i in range( len(a)/2, 0, -1):
        heapify(a,i)

def heapSort(a):
    
    buildHeap(a)
    for i in range(len(a), 1, -1):
        a[1], a[i] = a[i], a[1]
        


a = letturaArray()
#b = insertionSort(a)
#b = quickSort(a)
#b = mergeSort(a)
b = mergeSort(a)


print(b[0:len(a)])