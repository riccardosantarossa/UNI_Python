

#Tempo QUADRATICO
#def periodoFrazionario(s):
#
#    for p in range (1, len(s) +1 ):
#        corretto = True
#    
#    for i in range(0, len(s)):
#        if s[i] != s[i % p]:
#            corretto = False


def periodoFrazionarioEfficiente(s):
    
    bordo = ""
    
    for i in range (1, len(s)):
        if s[i] == s[len(s) - i]:
            bordo = s[i]
        
    print(bordo)
    
        
    
    
   


s = input()