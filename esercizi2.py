#es A 

for x in range(5):
    numero = int(input("Scrivere un numero:"))
    print (numero) 

print ("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø")

#es B 

listanum= []
for x in range(5):
    numero = int(input("Scrivere un numero:"))
    listanum.append(numero)

listanum.reverse()
print (listanum)

print ("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø")

# es C 

listanum= []
for x in range(5):
    n = int(input("Scrivere un numero:"))
    check = int(n/2)
    if check*2== n:
        listanum.append(n)

listanum.reverse()
print (listanum)

print ("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø")

#es D 

x= int(input("Quanti numeri si vuole inserire? "))
for y in range(x):
   n= int(input("Digitare un numero: "))
   print (n*n)


print ("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø")

#es E

def primo(n):
    if n == 0:
        print (n , "non è un numero primo")
    
    if n == 1:
        print (n , "non è un numero primo")   
        
    for y in range(2,n):
        if n%y == 0:
            print (n , "non è un numero primo")
            break
        else:
            print("True")
            break

primo(17)