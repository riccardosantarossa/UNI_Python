
#Lettura dell'array in input
def letturaArray():
    tokens = input().split(" ")
    return [int(x) for x in tokens if x]  # "if x" is for filtering out empty tokens

def findInterval(a, s):
    
    if len(a) == 0:
        return -1,-1
    
    i = 0
    j = 0
    sommaCorrente = a[j]
    
    while i < len(a) and j < len(a):  #sommaCorrente = a[i:j+1]
        
        if sommaCorrente == s:
            return i,j
        elif sommaCorrente < s:
            j += 1   
            sommaCorrente += a[j] if j < len(a) else 0  #aggiungo solo se sono nell'array
        else:
            i += 1
            sommaCorrente -= a[i-1] 
        
    return -1, -1

a = letturaArray()
s = int(input())

i,j = findInterval(a, s)
print(i,j)
