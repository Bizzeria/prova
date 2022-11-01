x = isinstance(5, int)                                              #6.1 operatore isinstance per verificare se un valore è integer (int)

x = isinstance("Hello", (float, int, str, list, dict, tuple))       #6.2 anche con diversi tipi elencati

class myObj:
  name = "John"

y = myObj()

x = isinstance(y, myObj)                                            #6.3 