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




