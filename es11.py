
def letturaArray():
    tokens = input().split(" ")
    return [int(x) for x in tokens if x]  # "if x" is for filtering out empty tokens

def majorityCandidate(a):
    
    c = 0
    majority = None
    
    for i in range(len(a)):
        
        if c == 0:
            majority = a[i]
            c += 1   
        else:
            if a[i] == majority:
                c += 1
            else:
                c -= 1 

    threshold = len(a) // 2
    count = 0
    
    for j in range(len(a)):
        
        if a[j] == majority:
            count += 1
    
    if count > threshold:
        return majority  
    else: 
        return "No majority" 
        
a = letturaArray()
print(majorityCandidate(a))
