a = 33
b = 200
if b > a:
  print("b is greater than a")            
                                                     #3.1 

a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error #3.2 scrivere print staccato 

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
  print("a is greater than b")                       #3.4 comando "sennò"

  a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")                   #3.5 anche senza elif

  if a > b: print("a is greater than b")             #3.6 anche senza dichiarare le variabili 