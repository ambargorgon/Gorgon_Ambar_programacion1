def most(a,b):
    #Realizar comparacion de parametros, no de variables globales
    if(a>b):
        #Devolver parametro
        return a
    else:
        return b

def least(a,b):
    if(a<b):
        return a
    else: 
        return b
    

x = int(input("Un numero: "))
y = int(input("Otro numero: "))

print(most(x-3, least(x+2, y-5)))

