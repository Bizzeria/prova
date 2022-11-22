def my_function():
  print("Hello from a function")
                                            #8.1 comando def per definire una funzione 

def my_function():
  print("Hello from a function")

my_function()                               #8.2 chiamare una funzione sennò non stampa 


def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")                      
                                            #8.3 cambiare la funzione (ne stampa 3)

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
                                            #8.4 due argomenti per una funzione

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")
                                            #8.5 errore: la funzione si aspetta due argomenti perchè ha due parametri

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
                                            #8.6 asterisco prima del parametro se non si sa quanti argomenti si avranno
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
                                            #8.7 con l'uguale non importa l'ordine degli argomenti rispetto ai parametri
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
                                            #8.8 due asterischi prima del parametro se usiamo l'uguale
                                            #    e non sappiamo quanti argomenti avremo 
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
                                            #8.9 in assenza di argomenti verrà usato il parametro

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
                                            #8.10 si possono usare liste come argomenti

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
                                            #8.11 operatore return per operazioni con le funzioni 

def myfunction():
  pass
                                            #8.12 operatore pass se funzione vuota per non dare errore

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

                                            #8.13 recursion fa si che funzione si chiami da sola