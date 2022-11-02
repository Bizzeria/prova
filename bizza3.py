a = 33
b = 200
if b > a:
  print("b is greater than a")            
                                                     #3.1 operatore if 

a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error 3.2 scrivere print staccato 

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")                         #3.3 comando "oppure se il primo è falso"

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")  
else:
  print("a is greater than b")                       #3.4 comando "in tutti gli altri casi"

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")                   #3.5 anche senza elif

if a > b: print("a is greater than b")             #3.6 anche senza dichiarare le variabili 

a = 2
b = 330
print("A") if a > b else print("B")                  #3.7 con una sola condizione da verificare

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
                                                     #3.8 tre condizioni in una riga sola

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")                  #3.9 operatore "and"

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")   #3.10 operatore "or"

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")                     #3.11 operatore if annidato 

a = 33
b = 200

if b > a:
  pass                                             #3.12 operatore "pass" se if vuoto

