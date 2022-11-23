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
    if n < 2:
        print (n , "non è un numero primo")   
    if n == 2:
        print ("true")    
    for y in range(2,n):
        if n%y == 0:
            print (n , "non è un numero primo")
            break
        else:
            print("true")
            break

primo(17)

prm = int(input("Scrivere un numero: "))
def primi(prm):      
    if prm < 2:
        print (prm, "non è un numero primo")   
    if prm == 2:
        print("primo")
    for s in range(2,prm):
        if prm%s == 0:
            print (prm , "non è un numero primo")
            break
        else:
            print ("primo")
        break

primi (prm)

print ("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø")

#es F

Sbommi = []

def lista(Sungro):
    for elem in Sbommi:
        for f in range(elem):
            print("*", end="")
        print("")

rn = int(input("Quanti numeri si vuole inserire? "))
for c in range (rn):
    num=int(input("Scrivere un numero: "))
    Sbommi.append(num)

lista(Sbommi)

print ("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø")

#es G

def Fibonacci(fib):
    if fib > 1:
        return Fibonacci(fib-1) + Fibonacci(fib-2)
    return fib

fib=int(input("Scrivere un numero: "))
Fibonacci(fib)

for g in range (1, fib+1):
    print (Fibonacci(g))

print ("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø")

#es H 

def wars(*parametri):
    print (parametri[2])
    print (parametri[3])
wars ("accidents", "crimes", 7, 25, "i_love_football")


print ("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø")

#es I

piani=int(input("Di quanti piani deve essere alto l'albero?: "))
for k in range(piani):
    print(" "*(piani-k-1) + "*"*(2*k+1))


print ("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø")