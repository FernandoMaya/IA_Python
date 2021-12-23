import math
import random

salir = False
opcion = 0


def factorial(n):
        if n > 1:
            return n * factorial(n - 1)
        else:
            return 1


def palabra():
    n=4 # de consonante vocal. pares
    con='bcdfghjklmnpqrstvwxyz'
    c = con.upper()
    vocal='aeiou'
    v = vocal.upper()
    L=[]
    
    for i in range(200):
        p=''
        for j in range(n):
            p+=''.join(random.choice(con))
            p+=''.join(random.choice(v))
        L.append(p)
    print (L)




while not salir:
    opcion = int(input("1. Ejercicio \n 2.Ejercicio\n 0. Salir\n"))
    
    if opcion == 1:
        num = int(input("Ingrese un numero: "))
        resultado = factorial(num)
        print(resultado)
        
    elif opcion == 2:
        palabra()
        
    elif opcion == 0:
        salir = True
        
    else:
        print("Numero incorrecto, elija uno del menu")
        

        

