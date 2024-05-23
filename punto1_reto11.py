#Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.
def suma (matriz1:list,matriz2:list,filas:int,columnas:int)->list: #Función para sumar matrices, recibe dos listas y dos enteros y devuelve una lista.
    matriz_suma = [] #Se inicializa la matriz resultante como una lista vacía.
    for i in range (filas): #Recorre las filas.
        fila_suma = [] #Lista vacía.
        for j in range(columnas): #Recorre cada elemento de la fila.
            suma = matriz1[i][j] + matriz2[i][j] #Se suman los elemntos en la posición i,j de cada matriz.
            fila_suma.append(suma) #Se añade el resultado de suma a la lista fila_suma.
        matriz_suma.append(fila_suma) #Se añade la lista fila_suma a la matriz.
    return matriz_suma #Se retorna matriz_suma.

def resta (matriz1:list,matriz2:list,filas:int,columnas:int)->list: #Función para restar matrices, recibe dos listas y dos enteros y devuelve una lista.
    matriz_resta = [] #Se inicializa la matriz resultante como una lista vacía.
    for i in range(filas): #Recorre las filas.
        fila_resta = [] #Lista vacía.
        for j in range(columnas): #Recorre cada elemento de la fila.
            resta = matriz1[i][j] - matriz2[i][j] #Se restan los elemntos en la posición i,j de cada matriz.
            fila_resta.append(resta) #Se añade el resultado de resta a la lista fila_resta.
        matriz_resta.append(fila_resta) #Se añade la lista fila_resta a la matriz.
    return matriz_resta #Se retorna matriz_resta.

#Matrices.
M1=[[1,2,3],[4,5,6],[7,8,9]] 
M2=[[2,4,6],[8,0,1],[3,5,7]]
M3=[[1,2],[8,9],[5,6]]
M4=[[1,0,2],[9,3,8],[4,7,5],[6,0,1]]
M5=[[3,4],[9,0],[7,8]]
M6=[[1,4,7],[2,5,8],[3,6,9],[0,2,6]]

#Se muestran las matrices disponibles.
print("Estas son las matrices que dispone para realizar operaciones: ")
print("----------")
print("Matriz 1:")
for i in range(len(M1)): #Para que la matriz se muestre de forma correcta y no como lista.
  print(M1[i])
print("----------")
print("Matriz 2:")
for i in range(len(M2)):
  print(M2[i])
print("----------")
print("Matriz 3:")
for i in range(len(M3)):
  print(M3[i])
print("----------")
print("Matriz 4:")
for i in range(len(M4)):
  print(M4[i])
print("----------")
print("Matriz 5:")
for i in range(len(M5)):
  print(M5[i])
print("----------")
print("Matriz 6:")
for i in range(len(M6)):
  print(M6[i])
print("----------")

operacion=input("¿Qué operación desea realizar? ('SUMA'/'RESTA'): ") #Se solicita elegir la operación a realizar.
#Se solicita elegir las matrices que se sumarán o restarán.
matriz1=input("Escriba M1/M2/M3/M4/M5/M6 dependiendo de qué matriz desea usar como primer término de la operación: ")
matriz2=input("Escriba M1/M2/M3/M4/M5/M6 dependiendo de qué matriz desea usar como segundo término de la operación: ")

#Se asigna la matriz seleccionada de primeras a m1.
#Se van evaluando los diferentes casos para ver qué eligió el usuario.
match matriz1:
        case "M1":
            m1=M1
        case "M2":
            m1=M2
        case "M3":
            m1=M3
        case "M4":
            m1=M4
        case "M5":
            m1=M5
        case "M6":
            m1=M6
        case _:
            m1=M1 #Caso por defecto, por si la entrada no es válida

#Se asigna la matriz seleccionada de segundas a m2.
#Se van evaluando los diferentes casos para ver qué eligió el usuario.
match matriz2:
        case "M1": 
            m2=M1
        case "M2":
            m2=M2
        case "M3":
            m2=M3
        case "M4":
            m2=M4
        case "M5":
            m2=M5
        case "M6":
            m2=M6
        case _:
            m2=M2 #Caso por defecto, por si la entrada no es válida

#Se imprimen de forma correcta las matrices elegidas.
for i in range(len(m1)):
  print(m1[i])
print("----------")
for i in range(len(m2)):
  print(m2[i])

#Se determina el número de filas y columnas de las matrices seleccionadas.
filas1=len(m1) #La longitud de m es el número de filas.
filas2=len(m2)
columnas1=len(m1[0]) #Como se sabe que las matrices tienen el mismo número de elementos en cada fila, se puede conocer el número de columnas con la longitud de la primera fila.
columnas2=len(m2[0])

if filas1==filas2 and columnas1==columnas2: #Se evalúa si las matrices son de igual tamaño para que se pueda realizar la operación.
    print("Las matrices son de igual tamaño, se puede realizar la operación.") #Se imprime mensaje de que sí se pueden sumar/restar.

    if operacion=="SUMA": #Si la operación elegida es SUMA:
        s=suma(m1,m2,filas1,columnas1) #Se evalúa la función suma con m1,m2,filas1 y columnas1 como argumentos. Esto se guarda en s.
        print("La suma de las matrices es:")
        for i in range(len(s)): #Se imprime la matriz resultante de la suma de las matrices elegidas.
            print(s[i])
    
    elif operacion=="RESTA": #Si la operación elegida es RESTA:
        r=resta(m1,m2,filas1,columnas1) #Se evalúa la función resta con m1,m2,filas1 y columnas1 como argumentos. Esto se guarda en r.
        print("La resta de las matrices es:")
        for i in range(len(r)): #Se imprime la matriz resultante de la resta de las matrices elegidas.
            print(r[i])

    else:
        print("La operación ingresada no es válida.") #Por si se escribió algo diferente a SUMA/RESTA en operacion.

else:
    print("Las matrices no son de igual tamaño, no se puede realizar la operación.") #Si las matrices son de diferente tamaño se imprime este mensaje.