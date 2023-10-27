raw_input = input

#Scrivere un programma che stampi tutti i prefissi di una stringa ricevuta in input.

s=raw_input()

for i in range (len(s)):
    
    print(s[0:len(s)-i])