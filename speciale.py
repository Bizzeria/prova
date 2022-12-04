def mcd (bommo):
    n = 0
    minimo = lista[n]# trovo il minimo
                    
    for a in reversed(range(1, minimo+1)): #-male che vada l'mcd è 1. L'mcd potrebbe essere anche il minimo
        candidato = True     #Questa variabile diventa false se almeno un numero nella lista non è divisibile per a
        for num in lista:
            if num%a != 0:    #se uno dei numeri non è divisibile per a allora a non è più un candidato              
                candidato = not True
        
        if candidato == True:
            return a
            n +=1
        

lista = []                      

elem = int(input("Quanti numeri si vuole inserire? "))  
 
for f in range (elem):
    numeri = int(input("Digita un numero: "))           
    lista.append(numeri) 

lista.sort()        #comodità
print (lista)


print (mcd(lista))
                         