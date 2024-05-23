#Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.
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