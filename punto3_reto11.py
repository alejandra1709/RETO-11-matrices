#Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.
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