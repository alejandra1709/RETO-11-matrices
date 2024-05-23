# RETO 11 - matrices
>***1. Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.***
```python
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
```
>***2. Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.***
```python
def producto (matriz1:list,matriz2:list,filas1:int,columnas1:int,columnas2:int)->list: #Función para multiplicar matrices, recibe dos listas y tres enteros y devuelve una lista.
    nueva_matriz=[] #Se inicializa la matriz resultante como una lista vacía.
    for i in range (filas1): #Recorre las filas de la primera matriz.
        fila_producto=[] #Se inicializa una lista vacía en donde se almacenarán las filas de la nueva matriz.
        for j in range (columnas2): #Recorre cada columna de la segunda matriz.
            mult=0 #Variable para almacenar la suma de los productos.
            for k in range (columnas1): #Recorre cada elemente de la fila y la columna correspondiente.
                x=matriz1[i][k] * matriz2[k][j] #Calcula el producto correspondiente y lo guarda en x.
                mult+=x #Se suma x a mult.
            fila_producto.append(mult) #Añade el resultado de la suma de productos (cada término) a la fila_producto.
        nueva_matriz.append(fila_producto) #Se añade la fila_producto (fila con los nuevos elementos) a la nueva matriz.
    return (nueva_matriz) #Se retorna la matriz resultante del producto entre matrices.

#Matrices.
M1=[[1,2,3],[4,5,6],[7,8,9]] 
M2=[[2,4,6],[8,0,1],[3,5,7]]
M3=[[1,2],[8,9],[5,6]]
M4=[[1,0,2],[9,3,8]]
M5=[[3,4],[9,0],[7,8],[1,5]]
M6=[[1,4,7,0],[6,2,5,8]]

#Se muestran las matrices disponibles.
print("Estas son las matrices que dispone para realizar el producto de matrices: ")
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

#Se solicita al usuario que seleccione las matrices que desea multiplicar.
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

#Se verifica si las matrices se pueden multiplicar.
if columnas1==filas2: #Para que se puedan multiplicar el número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.
    print("Las matrices se pueden multiplicar.") #Mensaje si sí se pueden multiplicar.
    mult=producto(m1,m2,filas1,columnas1,columnas2) #Se llama a la función producto y se dan los argumentos m1, m2, filas1, columnas1 y columnas2.
    print("El producto de las matrices es:") #Se imprime la matriz resultante del producto de las matrices elegidas.
    for i in range(len(mult)):
            print(mult[i])
else:
    print("Las matrices no se pueden multiplicar.") #Mensaje de error si las matrices no se pueden multiplicar.
```
>***3. Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.***
```python
def matriz_transpuesta(matriz:list)->list: #Función para obtener la matriz transpuesta, recibe una lista y devuelve otra lista.
    filas=len(matriz) #Número de filas de la matriz original.
    columnas=len(matriz[0]) #Número de columnas de la matriz original.
    nueva_matriz=[] #Se inicializa la matriz resultante como una lista vacía.

    for i in range (columnas): #Recorre cada columna de la matriz original.
        fila_nueva=[] #Lista para almacenar las filas nuevas.
        for j in range (filas): #Recorre cada fila de la matriz original.
            fila_nueva.append(matriz[j][i])  #Añade el elemento correspondiendte a la lista de fila_nueva.
        nueva_matriz.append(fila_nueva) #Se añaden las filas nuevas a la nueva_matriz.
    return(nueva_matriz) #Se devuelve la nueva_matriz.

#Se solicita al usuario que seleccione la cantidad de filas y columnas que tendrá la matriz.
filas=int(input("¿Cuántas filas quiere que tenga la matriz?: "))
columnas=int(input("¿Cuántas columnas quiere que tenga la matriz?: "))

matriz=[] #Lista vacía en donde se almacenará la matriz ingresada por el usuario.
for i in range(filas): #Itera sobre el rango del número de filas.
    fila=[] #Lista vacía para almacenar los elementos de cada fila ingresados.
    for j in range (columnas): #Itera sobre el rango del número de columnas.
       elemento=int(input("Ingrese elemento: ")) #Se solicita al usuario ingresar un elemento para la matriz.
       fila.append(elemento) #Se añade el elemento ingresado a la fila actual.
    matriz.append(fila) #Se añade la fila completa a la matriz.

#Se obtiene la matriz transpuesta, llamando a la función matriz_transpuesta y enviándole como argumento la matriz.
trans=matriz_transpuesta(matriz)

#Se imprime la matriz original y la matriz transpuesta.
print("La matriz original es:")
for i in range(len(matriz)):
  print(matriz[i])
print("-------------------------")
print("La matriz transpuesta es:")
for i in range(len(trans)):
  print(trans[i])
```
>***4. Desarrollar un programa que sume los elementos de una columna dada de una matriz.***
```python
def suma_columna (matriz:list,columna:int)->int: #Función para hallar la suma de los elementos de una columna, recibe una lista y un entero y retorna un entero.
    suma=0 #Se inicializa la variable suma en 0.
    for i in range (len(matriz)): #Recorre cada fila de la matriz.
        suma+=matriz[i][columna] #Se va sumando el elemento en la columna seleccionada de cada fila.
    return (suma) #Se retorna la suma.

#Matrices.
M1=[[1,2,3],[4,5,6],[7,8,9]] 
M2=[[2,4,6],[8,0,1],[3,5,7]]
M3=[[1,2],[8,9],[5,6]]
M4=[[1,0,2],[9,3,8]]
M5=[[3,4],[9,0],[7,8],[1,5]]
M6=[[1,4,7,0],[6,2,5,8]]

#Se muestran las matrices disponibles.
print("Estas son las matrices que dispone: ")
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

#Se solicita al usuario que seleccione una matriz y una columna de esta.
matriz1=input("Escriba M1/M2/M3/M4/M5/M6 dependiendo de qué matriz desea utilizar: ")
columna=int(input("Elija una columna para sumar sus elementos (tenga en cuenta que la primera columna es la número 0): "))

#Se asigna la matriz seleccionada a m1.
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

if columna<len(m1[0]): #Verifica si la columna ingresada es válida para la matriz seleccionada.
    suma=suma_columna(m1,columna) #Se evalúa la suma llamando la función suma_columna, enviándole como argumentos la matriz y columna seleccionadas.
    print("La suma de los elementos en la columna",columna,"de",matriz1,"es:",suma)

else: print("El número de columna no es válido para esta matriz.") #Mensaje de error si el número de columna ingresado no es válido.
```
>***5. Desarrollar un programa que sume los elementos de una fila dada de una matriz.***
```python
def suma_fila (matriz:list,fila:int)->int: #Función para hallar la suma de los elementos de una fila, recibe una lista y un entero y retorna un entero.
    suma=0  #Se inicializa la variable suma en 0.
    for i in range (len(matriz[0])): #Recorre cada columna de la matriz.
        suma+=matriz[fila][i] #Se va sumando el elemento en la fila seleccionada de cada columna.
    return (suma) #Se retorna la suma.

#Matrices.
M1=[[1,2,3],[4,5,6],[7,8,9]] 
M2=[[2,4,6],[8,0,1],[3,5,7]]
M3=[[1,2],[8,9],[5,6]]
M4=[[1,0,2],[9,3,8]]
M5=[[3,4],[9,0],[7,8],[1,5]]
M6=[[1,4,7,0],[6,2,5,8]]

#Se muestran las matrices disponibles.
print("Estas son las matrices que dispone: ")
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

#Se solicita al usuario que seleccione una matriz y una fila de esta.
matriz1=input("Escriba M1/M2/M3/M4/M5/M6 dependiendo de qué matriz desea utilizar: ")
fila=int(input("Elija una fila para sumar sus elementos (tenga en cuenta que la primera fila es la número 0): "))

#Se asigna la matriz seleccionada a m1.
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

if fila<len(m1): #Verifica si la fila ingresada es válida para la matriz seleccionada.
    suma=suma_fila(m1,fila) #Se evalúa la suma llamando la función suma_fila, enviándole como argumentos la matriz y fila seleccionadas.
    print("La suma de los elementos en la fila",fila,"de",matriz1,"es:",suma)

else: print("El número de fila no es válido para esta matriz.") #Mensaje de error si el número de fila ingresado no es válido.
```

