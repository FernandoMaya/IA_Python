import math
import random
# import numpy as np
# def takeSecond(elem):
#     return elem[3]

alfabeto = 'abcdefghijklmnñopqrstuvwxyz'         #Definición de alelos
L = []                                           #Lista vacia

for i in range(200):                           #definimos el tamaño de la población
    p = ''
    p= ''.join(random.choices(alfabeto, k = 8)) #Definimos la longitud de la palabra (el genotipo)
    a = str(p.count("a"))                       # En esta etapa contamos el numero de veces que aparece la "A"
    L.append(a + p)                             #Concatenamos el valor de a al inicio de cada palabra
    L_mayusculas = [x.upper() for x in L]       #Cambiamos a mayusculas la lista
    L_mayusculas.sort(reverse=True)             #Ordenamos la lista de mayor a menor
    
# print (L_mayusculas)

ranking = 0

for i in L_mayusculas:
    ranking = ranking+1
    if ranking <10:
        L_mayusculas[ranking-1] = (str("00") + str(ranking) + i)
        print(str("00") + str(ranking) + i)
    elif 10 <= ranking <100:
        L_mayusculas[ranking-1]=(str("0") + str(ranking) + i)
        print (str("0") + str(ranking) + i)
    else:
        L_mayusculas[ranking-1]= (str(ranking) +i)
        print (str(ranking) +i)
        
###############Steady State Selection################
Lista_100 = L_mayusculas[:len(L_mayusculas)//2] #Dividir lista rankeada en 2
print("\n\n\n########################################\n\n\n")
for i in Lista_100:                             #Para imprimir en orden hacemos un for de la nueva lista de 100
    print (i)
print("\n\n\n########################################\n\n\n")
################## TOURNAMENT SLECTION ########################################
Lista_T = []
for veces in range(100):		 
	num1 = random.sample(L_mayusculas, 1) 
	num2 = random.sample(L_mayusculas, 1) 

	while (num1[0] == num2[0]):   
		num2 = random.sample(L_mayusculas, 1)
	
	num4 = num1[0]
	num5 = num2[0]	   

	
	if(num4<num5):					
		Lista_T.append(num1[0])	
		L_mayusculas.remove(num2[0])		
		L_mayusculas.remove(num1[0])

	else:							
		Lista_T.append(num2[0])
		L_mayusculas.remove(num1[0])
		L_mayusculas.remove(num2[0])
for i in Lista_T:
    print(i)

print("\n\n\n########################################\n\n\n")
copia_t = Lista_T
Single_point = []
contador = 0
c = 50
g = 200
for i in range (c):
		padre1_v2 = random.sample(copia_t, 1)  #Se ingresa la copia del tournament para poder seguir usando el arreglo
		padre1 = padre1_v2[0]
		padre2_v2 = random.sample(copia_t, 1)  
		padre2 = padre2_v2[0]

		while (padre1 == padre2):   
			padre2_v2 = random.sample(copia_t, 1)
			padre2 = padre2_v2[0]
		
		hijo1 = padre1[4:8]+padre2[8:]	
		hijo2 = padre2[4:8]+padre1[8:]
		
		contar_A = hijo1.count("A")
		contador += contar_A	   					
		converted = str(contar_A) 
		hijo1_1 = hijo1  				

		contar_A = hijo2.count("A")
		contador += contar_A	
		converted = str(contar_A) 
		hijo2_1 = hijo2 
		
		V_a = padre1[3]  
		contador += int(V_a)
		V_a = padre2[3]
		contador += int(V_a)
		Single_point.append(padre1[4:]) 			
		Single_point.append(padre2[4:])				
			
		copia_t.remove(padre1)
		copia_t.remove(padre2)						
		
		Single_point.append(hijo1_1)				
		Single_point.append(hijo2_1)				
Single_point.sort(reverse=True)
for i in Single_point:
    print (i)
for y in range(g):			
	x = str (y).zfill(4)	
	Single_point[y] = x+Single_point[y]
print("\n\n\n########################################\n\n\n")

print(hijo1[0:] + "\n" + hijo2[0:])
print(padre1[0:] + "\n" + padre2[0:])