# 12. Hacer una función para que imprima un arreglo o lista de 10 elementos numéricos insertados uno por uno y ordenados 
# de forma ascendente y mostrarlos en pantalla.

def imprimir_arreglo(): # Función para imprimir un arreglo de 10 elementos numéricos ordenados de forma ascendente
    arreglo = [] # Crear una lista vacía para almacenar los números ingresados por el usuario
    for i in range(10): # Bucle para solicitar al usuario que ingrese 10 números
        numero = float(input(f"Ingrese el número {i+1}: ")) # Solicitar al usuario que ingrese un número y convertirlo a float
        arreglo.append(numero) # Agregar el número ingresado a la lista
    
    arreglo.sort() # Ordenar el arreglo de forma ascendente utilizando el método sort() de la lista, este método ordena la lista en su lugar,es decir, modifica la lista original
    
    print("Arreglo ordenado de forma ascendente:") # Imprimir un mensaje indicando que el arreglo ha sido ordenado
    for numero in arreglo: # Bucle para imprimir cada número en el arreglo ordenado
        print(numero)   
imprimir_arreglo()  # Llamar a la función para ejecutar el programa

# Otra forma de hacerlo sin usar el método sort()
def imprimir_arreglo(): # Función para imprimir un arreglo de 10 elementos numéricos ordenados de forma ascendente
    arreglo = [] # Crear una lista vacía para almacenar los números ingresados por el usuario
    for i in range(10): # Bucle para solicitar al usuario que ingrese 10 números
        numero = float(input(f"Ingrese el número {i+1}: ")) # Solicitar al usuario que ingrese un número y convertirlo a float
        arreglo.append(numero) # Agregar el número ingresado a la lista
    
    # Ordenar el arreglo de forma ascendente utilizando un algoritmo de ordenamiento (por ejemplo, el método de burbuja), este método compara cada elemento con el siguiente y los intercambia si están en el orden incorrecto, repitiendo este proceso hasta que la lista esté ordenada
    for i in range(len(arreglo)): # Bucle para recorrer cada elemento del arreglo
        for j in range(i + 1, len(arreglo)): # Bucle para comparar el elemento actual con los siguientes elementos del arreglo
            if arreglo[i] > arreglo[j]: # Si el elemento actual es mayor que el siguiente elemento, se intercambian los elementos
                arreglo[i], arreglo[j] = arreglo[j], arreglo[i] # Intercambiar los elementos utilizando una asignación múltiple, donde el elemento actual toma el valor del siguiente elemento y el siguiente elemento toma el valor del elemento actual
    
    print("Arreglo ordenado de forma ascendente:") # Imprimir un mensaje indicando que el arreglo ha sido ordenado
    for numero in arreglo: # Bucle para imprimir cada número en el arreglo ordenado
        print(numero) # Llamar a la función para ejecutar el programa
imprimir_arreglo()  # Llamar a la función para ejecutar el programa
