fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)                                              #4.1 operatore for per ripetere qualcosa di una lista

for x in "banana":
  print(x)                                              #4.2 operatore for per ripetere le lettere di una parola

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break                                               #4.3 operatore break ferma il loop alla condizione dettata dall if

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)                                              #4.4 operatore break prima di stampare 

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)                                              #4.5 operatore "continue" per ignorare la condizione dettata da if

for x in range(6):
  print(x)                                              #4.6 funzione "range(x)" stampa numeri fino a x escluso

for x in range(2, 6):
  print(x)                                              #4.7 da 2 a 6 escluso

for x in range(2, 30, 3):
  print(x)                                              #4.8 stampa un numero ogni 3 numeri da 2 a 30 escluso

for x in range(6):
  print(x)
else:
  print("Finally finished!")                            #4.9 stampa qualcosa con else finito il loop

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")                            #4.10 else non funziona se c'è break 

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)                                         #4.11 operatori for annidati 

for x in [0, 1, 2]:
  pass                                                  #4.12 se for non ha contenuti metti pass
