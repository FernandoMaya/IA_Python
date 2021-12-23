
"Funcion en AG"
#sss 000-100  = 100
#st 000-200  = 100
import random
frase=[]		#arreglo de 200, Este arreglo desaparece
Tournament =[]
copia =[]		#arreglo de 100 de SSS

Single_point =[]    #Arreglos final de single point, multiple point y uniform
Single_point_2 =[]
Multiple_point = []	
Multiple_point_2 =[]
Uniform =[]
Uniform_2=[]
Contador_a = 0     #Contadores para a
Contador_a_2 =0
Contador_SP =0		#Contadores para single point. primeros 100 y Tournament
Contador_SP_2 =0
Contador_Mp = 0     #Contadores para Multiple point. "" "" "" ""
Contador_Mp_2 =0
Contador_U = 0		#Contadores para Uniform. """"""
Contador_U_2 =0

ArregloSP =[]       #Arreglos que guardan la fitness funtion, se imprimen como arreglo y un texto que las define
ArregloSP2 = []
ArregloMP =[]
ArregloMP2 =[]
ArregloUniform =[]   
ArregloUniform2 =[]

def id_generator(size=8, chars='ABCDEFGHIJKLMNOÑPQRSTUVWXYZ'):
	return ''.join(random.choice(chars) for _ in range(size))   #funcion para generar palabras aleatorias

n = 200
m = 50 						#repeticiones para operadores de cruzamiento
for i in range(n):			#For para repetir las palabras necesarias
	sale = id_generator() 	#variable para guardar el return del def
	AS = sale.count("A")	#variable para guardar las A's contadas		
	converted = str(AS) 	#AS es un int y no concatena con string, volverlo str
	final = converted+sale  #var para concatenar
	frase.append(final)  	#agregar al arreglo frase
							#Sin ordenar
frase.sort(reverse=True) 	#para acomodar

for y in range(n):			#for para agregar los numeros
	x = str (y).zfill(3)	#convertir los numeros a str, no funciona con int, zfill para formato de numeros 000
	frase[y] = x+"-"+frase[y] 
#print("---------------------Poblacion de 200--------------------------------------------------------------------")
#print("ordenado:",frase)		#Ordenado

for x in range(100):			#Toma los primeros 100
	copia.append(frase[x])
print("---------------------SSS-------------------------------------------------------------------")
#print(copia)
copia_1  = copia[:]   #copia de los primeros 100 para usarla, : es para no afectar al original
copia_2  = copia[:]
copia_3  = copia[:]

for contador in range(100):   					#Funcion contador de A's para copia
	Separador_frase =copia[contador].split("-") #Separa las frases por -
	NumeroA = Separador_frase[1]				#Se guarda la posicion 1
	Contador_a += int(NumeroA[0])				#Es un str, se accede al numero con [0], se guarda y se repite
print ("A's de los primeros 100: ",Contador_a)	#a's de la copia
#ST
for veces in range(100):		 
	num1 = random.sample(frase, 1) #Se declaran los "competidores", random.sample permite sacar valores del array al azar
	num2 = random.sample(frase, 1) #Se guardan como un "array"

	while (num1[0] == num2[0]):    #Existe la posibilidad de tronar porque puede tomar un numero igual en num1 y num2, para esto es.
		num2 = random.sample(frase, 1)
	
	num4 = num1[0].split("-")      #Separar por - para mas facil. Esto retorna un array, se toma la posicion 0
	num5 = num2[0].split("-")	   #y se guarda en otras variables.

	
	if(num4<num5):					#Si num1 es menor a num2 entonces gana num1
		Tournament.append(num1[0])	#Nuevo arreglo para guardar los numeros ganadores
		frase.remove(num2[0])		#Ambos numeros se eliminan para que no se repitan
		frase.remove(num1[0])

	else:							#Si no es asi, lo contrario
		Tournament.append(num2[0])
		frase.remove(num1[0])
		frase.remove(num2[0])

print("-----------------------Ganadores-ST-------------------------------------------------------------------")
#print(Tournament)
copia1_1 = Tournament[:]  #Copias de arreglo al azar, : para no afectar al original
copia1_2 = Tournament[:]
copia1_3 = Tournament[:]

#SSS son 100, salen 200-200-200

for contador in range(100):							#Contador de las a's al azar
	Variable_a = Tournament[contador].split("-")  
	NumeroA = Variable_a[1]	
	Contador_a_2 += int(NumeroA[0])	

print ("A's del Torneo al azar: ",Contador_a_2)

#Algoritmo para operadores de cruzamiento Single Point
for a in range (100):
	for i in range (m):  #50
		padre1_v2 = random.sample(copia_1, 1)  #regresa en un arreglo en posicion  0
		padre1 = padre1_v2[0]
		padre2_v2 = random.sample(copia_1, 1)  #arreglo de 100
		padre2 = padre2_v2[0]

		while (padre1 == padre2):   
			padre2_v2 = random.sample(copia_1, 1)
			padre2 = padre2_v2[0]
		
		#000-0ABCDEFGH
		hijo1 = padre1[5:10]+padre2[10:]	#Creacion del hijo con partes del padre1 y padre2
		hijo2 = padre2[5:10]+padre1[10:]
		
		AS = hijo1.count("A")
		Contador_SP += AS	   					#Contador de A para Single Point de los primeros 100
		converted = str(AS) 
		hijo1_1 = converted+hijo1  				#hijo sin los numeros

		AS = hijo2.count("A")
		Contador_SP += AS	
		converted = str(AS) 
		hijo2_1 = converted+hijo2 
		
		Variable_a = padre1[4]  
		Contador_SP += int(Variable_a)
		Variable_a = padre2[4]
		Contador_SP += int(Variable_a)
		Single_point.append(padre1[4:]) 			#Se agregan los padres al arreglo single_point.
		Single_point.append(padre2[4:])				#como se tiene que ordenar de nuevo, quito los numeros de al principio
			
		copia_1.remove(padre1)
		copia_1.remove(padre2)						#Se borran para que no se repitan, este arregla quedara en 0
		
		Single_point.append(hijo1_1)				#Agregamos al hijo1 con el formato requerido
		Single_point.append(hijo2_1)				#Agregamos al hijo2 con el formato requerido

	Single_point.sort(reverse=True)

	for y in range(n):			#for para agregar los numeros
		x = str (y).zfill(3)	#convertir los numeros a str, no funciona con int, zfill para formato de numeros 000
		Single_point[y] = x+"-"+Single_point[y] 

	#print("A's del Single_point de Sss:     ", Contador_SP, a)					#Total de A de single Point
	ArregloSP.append(Contador_SP) 					#Se agrega el valor de FF a un nuevo array antes de perderlo
	Contador_SP = 0
	#tomar los 100 mejores
	p =100
	del Single_point[-p:]							#Funcion que permite eliminar la mitad de la poblacion, los 
	#print(Single_point)							#100 mejores quedan
	copia_1 = Single_point [:]						#Una vez quedados los 100 pasan a una copia, ahora sera la nueva poblacion
	Single_point = []								#Se borra el array para poder reutilizarse x veces
	
print("Arreglo SP de SSS: ", ArregloSP)
#Repiticion de la misma documentacion
#Algoritmo para operadores de cruzamiento Multiple point
for a in range (100):
	for i in range (m):	
		padre1_v2 = random.sample(copia_2, 1)
		padre1 = padre1_v2[0]
		padre2_v2 = random.sample(copia_2, 1)
		padre2 = padre2_v2[0]

		while (padre1 == padre2):    #Existe la posibilidad de tronar porque puede tomar un numero igual en padre1 y padre2, para esto es.
			padre2_v2 = random.sample(copia_2, 1)
			padre2 = padre2_v2[0]
				
		hijo1 = padre1[5:7]+padre2[7:10]+padre1[10:]
		hijo2 = padre2[5:7]+padre1[7:10]+padre2[10:]

		AS = hijo1.count("A")
		Contador_Mp += AS 					#Contador para A de Multiple point
		converted = str(AS) 
		hijo1_1 = converted+hijo1

		AS = hijo2.count("A")
		Contador_Mp += AS	
		converted = str(AS) 
		hijo2_1 = converted+hijo2 

		Variable_a = padre1[4]  #No funciona el anterior y esto es otra cosa que nose, cambio toda la frase a str
		Contador_Mp += int(Variable_a)			
		Variable_a = padre2[4]
		Contador_Mp += int(Variable_a)

		Multiple_point.append(padre1[4:])
		Multiple_point.append(padre2[4:])

		copia_2.remove(padre1)
		copia_2.remove(padre2)

		Multiple_point.append(hijo1_1)
		Multiple_point.append(hijo2_1)

	Multiple_point.sort(reverse=True)
	for y in range(n):			#for para agregar los numeros
		x = str (y).zfill(3)	#convertir los numeros a str, no funciona con int, zfill para formato de numeros 000
		Multiple_point[y] = x+"-"+Multiple_point[y] 
	#print("A's del Multiple_point de ST: ",Contador_Mp, a) #Total de A en el arreglo Multiple Points
	#print(Multiple_point)
	ArregloMP.append(Contador_Mp)
	Contador_Mp = 0
		#tomar los 100 mejores
	p =100
	del Multiple_point[-p:]
	#print(Multiple_point)
	copia_2= Multiple_point [:]
	Multiple_point = []
				
print("Arreglo MP de SSS: ", ArregloMP)

#Uniform
for a in range(100):
	for i in range (m):
		padre1_v2 = random.sample(copia_3, 1)
		padre1 = padre1_v2[0]
		padre2_v2 = random.sample(copia_3, 1)
		padre2 = padre2_v2[0]
		
		while (padre1 == padre2):   
			padre2_v2 = random.sample(copia_3, 1)
			padre2 = padre2_v2[0]

		#000-0ABCDEFGH
		hijo1 = padre1[5]+padre2[6]+padre1[7]+padre2[8]+padre1[9]+padre2[10]+padre1[11]+padre2[12]
		hijo2 = padre2[5]+padre1[6]+padre2[7]+padre1[8]+padre2[9]+padre1[10]+padre2[11]+padre1[12]
		
		AS = hijo1.count("A")
		Contador_U += AS					#Contador para A de Uniform
		converted = str(AS) 
		hijo1_1 = converted+hijo1

		AS = hijo2.count("A")	
		Contador_U += AS
		converted = str(AS) 
		hijo2_1 = converted+hijo2 
				
		Variable_a = padre1[4]  #No funciona el anterior y esto es otra cosa que nose, cambio toda la frase a str
		Contador_U += int(Variable_a)
		Variable_a = padre2[4]
		Contador_U += int(Variable_a)

		Uniform.append(padre1[4:])
		Uniform.append(padre2[4:])
		
		copia_3.remove(padre1)
		copia_3.remove(padre2)
		
		Uniform.append(hijo1_1)
		Uniform.append(hijo2_1)

	Uniform.sort(reverse=True)

	for y in range(n):			#for para agregar los numeros
		x = str (y).zfill(3)	#convertir los numeros a str, no funciona con int, zfill para formato de numeros 000
		Uniform[y] = x+"-"+Uniform[y] 
	#print("A's del Uniform de ST:       ",Contador_U)			#Total de A en Uniform
	#print(Uniform)
	ArregloUniform.append(Contador_U)
	Contador_U = 0
	#tomar los 100 mejores
	p =100
	del Uniform[-p:]
	copia_3= Uniform [:]
	Uniform = []
print("Arreglo U de SSS: ", ArregloUniform)					
#Tournament Operadores de cruzamientos Single point
for a in range(100):
	for i in range (m):
		padre1_v2 = random.sample(copia1_1, 1)
		padre1 = padre1_v2[0]
		padre2_v2 = random.sample(copia1_1, 1)
		padre2 = padre2_v2[0]
		

		while (padre1 == padre2):   
			padre2_v2 = random.sample(copia1_1, 1)
			padre2 = padre2_v2[0]
		#000-0ABCDEFGH
		hijo1 = padre1[5:10]+padre2[10:]  #Esta guardado como un valor dentro un array y dentro de otro
		hijo2 = padre2[5:10]+padre1[10:]  #asi que solo con doble [0] funciona

		AS = hijo1.count("A")
		Contador_SP_2 += AS							  #Contador para single point pero con tournament
		converted = str(AS) 
		hijo1_1 = converted+hijo1

		AS = hijo2.count("A")
		Contador_SP_2 += AS
		converted = str(AS) 
		hijo2_1 = converted+hijo2 
		
		Variable_a = padre1[4]  					#doble [0] para acceder a la posicion
		Contador_SP_2 += int(Variable_a)
		Variable_a = padre2[4]
		Contador_SP_2 += int(Variable_a)
		
		Single_point_2.append(padre1[4:])					#Arrelglo especial para single point de tournament
		Single_point_2.append(padre2[4:])
		
		copia1_1.remove(padre1)
		copia1_1.remove(padre2)

		Single_point_2.append(hijo1_1)
		Single_point_2.append(hijo2_1)
		
	Single_point_2.sort(reverse= True)
	for y in range(n):			#for para agregar los numeros
		x = str (y).zfill(3)	#convertir los numeros a str, no funciona con int, zfill para formato de numeros 000
		Single_point_2[y] = x+"-"+Single_point_2[y] 
	#print(Single_point_2)
	#print("A's de Single_point Tournament: ", Contador_SP_2)
	ArregloSP2.append(Contador_SP_2)
	Contador_SP_2 = 0
	#tomar los numeros al azar de SSS
	
	for veces in range(100):		 
		num1_V2 = random.sample(Single_point_2, 1) #Se declaran los "competidores", random.sample permite sacar valores del array al azar
		num1 = num1_V2[0]
		num2_V2 = random.sample(Single_point_2, 1) #Se guardan como un "array"
		num2 = num2_V2[0]

		while (num1 == num2):    #Existe la posibilidad de tronar porque puede tomar un numero igual en num1 y num2, para esto es.
			num2_V2 = random.sample(Single_point_2, 1)
			num2 = num2_V2[0]
		
		num4 = num1.split("-")      #Separar por - para mas facil. Esto retorna un array, se toma la posicion 0
		num5 = num2.split("-")	   #y se guarda en otras variables.

		
		if(num4<num5):				#Si num1 es menor a num2 entonces gana num1
			copia1_1.append(num1)	#Nuevo arreglo para guardar los numeros ganadores
			Single_point_2.remove(num2)	#Ambos numeros se eliminan para que no se repitan
			Single_point_2.remove(num1)

		else:						#Si no es asi, lo contrario
			copia1_1.append(num2)
			Single_point_2.remove(num1)
			Single_point_2.remove(num2)
		
	#print(copia1_1)
print("Arreglo SP de ST: ", ArregloSP2)	
#Multiple point tournament
for a in range(100):
	for i in range (m):	
		padre1_v2 = random.sample(copia1_2, 1)
		padre1 = padre1_v2[0]
		padre2_v2 = random.sample(copia1_2, 1)
		padre2 = padre2_v2[0]

		while (padre1== padre2):    
			padre2_v2 = random.sample(copia1_2, 1)
			padre2 = padre2_v2[0]	
					
		hijo1 = padre1[5:7]+padre2[7:10]+padre1[10:]
		hijo2 = padre2[5:7]+padre1[7:10]+padre2[10:]

		AS = hijo1.count("A")	
		Contador_Mp_2 += AS
		converted = str(AS) 
		hijo1_1 = converted+hijo1

		AS = hijo2.count("A")
		Contador_Mp_2 += AS	
		converted = str(AS) 
		hijo2_1 = converted+hijo2 

		Variable_a = padre1[4]  
		Contador_Mp_2 += int(Variable_a)
		Variable_a = padre2[4]
		Contador_Mp_2 += int(Variable_a)

		Multiple_point_2.append(padre1[4:])
		Multiple_point_2.append(padre2[4:])

		copia1_2.remove(padre1)
		copia1_2.remove(padre2)

		Multiple_point_2.append(hijo1_1)
		Multiple_point_2.append(hijo2_1)

	Multiple_point_2.sort(reverse=True)

	for y in range(n):			#for para agregar los numeros
		x = str (y).zfill(3)	#convertir los numeros a str, no funciona con int, zfill para formato de numeros 000
		Multiple_point_2[y] = x+"-"+Multiple_point_2[y] 
	
	#print(Multiple_point_2)
	#print("A's de Multiple_point Tournament: ",Contador_Mp_2)
	ArregloMP2.append(Contador_Mp_2)
	Contador_Mp_2 = 0

	#tomar los numeros al azar de SSS

	for veces in range(100):		 
			num1_V2 = random.sample(Multiple_point_2, 1) #Se declaran los "competidores", random.sample permite sacar valores del array al azar
			num1 = num1_V2[0]
			num2_V2 = random.sample(Multiple_point_2, 1) #Se guardan como un "array"
			num2 = num2_V2[0]

			while (num1 == num2):    #Existe la posibilidad de tronar porque puede tomar un numero igual en num1 y num2, para esto es.
				num2_V2 = random.sample(Multiple_point_2, 1)
				num2 = num2_V2[0]
			
			num4 = num1.split("-")      #Separar por - para mas facil. Esto retorna un array, se toma la posicion 0
			num5 = num2.split("-")	   #y se guarda en otras variables.

			
			if(num4<num5):				#Si num1 es menor a num2 entonces gana num1
				copia1_2.append(num1)	#Nuevo arreglo para guardar los numeros ganadores
				Multiple_point_2.remove(num2)	#Ambos numeros se eliminan para que no se repitan
				Multiple_point_2.remove(num1)

			else:						#Si no es asi, lo contrario
				copia1_2.append(num2)
				Multiple_point_2.remove(num1)
				Multiple_point_2.remove(num2)

print("Arreglo MP de ST: ", ArregloMP2)
#Uniform de tournament
for a in range(100):
	for i in range (m):
		padre1_v2 = random.sample(copia1_3, 1)
		padre1 = padre1_v2[0]
		padre2_v2 = random.sample(copia1_3, 1)
		padre2 = padre2_v2[0]
		
		while (padre1 == padre2):    
			padre2_v2 = random.sample(copia1_3, 1)
			padre2 = padre2_v2[0]

		#000-0ABCDEFGH
		hijo1 = padre1[5]+padre2[6]+padre1[7]+padre2[8]+padre1[9]+padre2[10]+padre1[11]+padre2[12]
		hijo2 = padre2[5]+padre1[6]+padre2[7]+padre1[8]+padre2[9]+padre1[10]+padre2[11]+padre1[12]
		
		AS = hijo1.count("A")
		Contador_U_2 += AS	
		converted = str(AS) 
		hijo1_1 = converted+hijo1

		AS = hijo2.count("A")	
		Contador_U_2 += AS
		converted = str(AS) 
		hijo2_1 = converted+hijo2 
				
		Variable_a = padre1[4]  
		Contador_U_2 += int(Variable_a)
		Variable_a = padre2[4]
		Contador_U_2 += int(Variable_a)

		Uniform_2.append(padre1[4:])
		Uniform_2.append(padre2[4:])
		
		copia1_3.remove(padre1)
		copia1_3.remove(padre2)

		Uniform_2.append(hijo1_1)
		Uniform_2.append(hijo2_1)
		
	Uniform_2.sort(reverse=True)

	for y in range(n):			#for para agregar los numeros
			x = str (y).zfill(3)	#convertir los numeros a str, no funciona con int, zfill para formato de numeros 000
			Uniform_2[y] = x+"-"+Uniform_2[y] 
	#print(Uniform_2)
	#print("A's de Uniform_2 de tournament: ",Contador_U_2)

	ArregloUniform2.append(Contador_U_2)

	Contador_U_2 = 0

	for veces in range(100):		 
				num1_V2 = random.sample(Uniform_2, 1) #Se declaran los "competidores", random.sample permite sacar valores del array al azar
				num1 = num1_V2[0]
				num2_V2 = random.sample(Uniform_2, 1) #Se guardan como un "array"
				num2 = num2_V2[0]

				while (num1 == num2):    #Existe la posibilidad de tronar porque puede tomar un numero igual en num1 y num2, para esto es.
					num2_V2 = random.sample(Uniform_2, 1)
					num2 = num2_V2[0]
				
				num4 = num1.split("-")      #Separar por - para mas facil. Esto retorna un array, se toma la posicion 0
				num5 = num2.split("-")	   #y se guarda en otras variables.

				
				if(num4<num5):				#Si num1 es menor a num2 entonces gana num1
					copia1_3.append(num1)	#Nuevo arreglo para guardar los numeros ganadores
					Uniform_2.remove(num2)	#Ambos numeros se eliminan para que no se repitan
					Uniform_2.remove(num1)

				else:						#Si no es asi, lo contrario
					copia1_3.append(num2)
					Uniform_2.remove(num1)
					Uniform_2.remove(num2)


print("Arreglo U de ST: ", ArregloUniform2)