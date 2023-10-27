raw_input = input

#Scrivere un programma che riceva su una riga di input una stringa (con possibili spazi) e in output produca la stessa stringa in ordine inverso.

s = raw_input()
a= ""

for i in range(len(s)-1, -1, -1):
    a += s[i];
    
print(a)
    