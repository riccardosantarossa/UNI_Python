
#Lettura dell'array in input
def letturaArray():
    tokens = input().split(" ")
    return [int(x) for x in tokens if x]  # "if x" is for filtering out empty tokens


#Prima soluzione con due cicli for, tempo QUADRATICO
#a = letturaArray()
#s = int(input())
#
#for i in range(0, len(a)):
#    for j in range(i+1, len(a)):
#        if(a[i] + a[j]) == s:
#            print(f"{i} {j}")
#            exit()
            
#print(-1,-1)


#Soluzione efficiente in tempo LINEARE
a = letturaArray()
s = int(input())

i = 0
j = len(a) - 1

while i < j:
  
  if a[i] + a[j] == s:
      print(f"{i} {j}")
      exit()
  elif a[i] + a[j] > s:
      j -= 1
  else:
      i += 1

print(-1,-1)