#es 1
x = "cane"
y = "mucca"
z = "cavallo"
s = "coccodrillo"
t = "falena"

print (x , y , z , t , s)

#es 2 

x = 5
y = 34
if x > y: 
    print ("ciao")
else: 
    print ("arrivederci")

x = 300 
y = 5
z = 57
if x >y and x > z:
    print ("x è il numero maggiore")

#es 4 
x = 300 
y = 5
z = 57
if x >y and x > z:
    print (x)
elif y > x and y > z:
    print (y)
elif z>x and z>y: 
    print (z)

#es 5
città = ["Ravenna", "torino", "milano"]
persone = ["Sungro", "RaphasamsonGAH"]

for x in città: 
    for y in persone: 
        print (x,y)

#es 6
import random 
numeri = []
u = 56
for x in range(5):
    rnd = random.randrange(1,7000)
    numeri.append(rnd)
    if u < rnd:
        print (rnd)

#es 7 
import random 
numeri = []
for x in range(5):
    rnd = random.randrange(1,70000)
    numeri.append(rnd)
  
for y in numeri: 
    minimo = numeri [0]
    if y < minimo:
      z=y
print(minimo)

#es 8
animali = ["mucca" , "cavallo" , "elicottero" , "elefante tandem psichico da guerra" , "scoiattolo"]
animali.reverse()
print (animali)

#es 9
animali = ["cane", "gatto", "leone"]
numeri = [19,22,34,47,89]

z = animali + numeri 
print (z)
for x in numeri: 
     if x>5: 
       print (x)

#es 10 

import random 
numeri = []
for x in range(10):
    rnd = random.randrange(1,70000)
    numeri.append(rnd)
print (numeri)
for y in numeri:
   check = int(y/2)
   if y == (check * 2):
   	   print(y)



