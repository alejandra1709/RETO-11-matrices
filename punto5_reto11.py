#Desarrollar un programa que sume los elementos de una fila dada de una matriz.
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