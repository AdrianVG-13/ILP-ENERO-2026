# 11. Pedir números enteros en un ciclo mientras sean positivos y en caso de que un número sea negativo cerrar el ciclo y al final promediar los números positivos ingresados por el usuario.

#USANDO UNA LISTA PARA ALMACENAR LOS NÚMEROS POSITIVOS

# ENTRADA DE DATOS
# numeros = []  # Lista para almacenar los números positivos ingresados por el usuario
# while True:
#     numero = int(input("Ingrese un número entero (negativo para salir): "))
#     if numero < 0:
#         break  # Salir del ciclo si el número es negativo
#     numeros.append(numero)  # Agregar el número positivo a la lista

# # PROCESOS (Cálculos u operaciones matemáticas y/o lógicas)
# if len(numeros) > 0:  # Verificar si se ingresaron números positivos
#     promedio = sum(numeros) / len(numeros)  # Calcular el promedio de los números positivos
#     print("El promedio de los números positivos ingresados es:", round(promedio, 2))
# else:
#     print("No se ingresaron números positivos para calcular el promedio.")  

# Otra forma de calcular el promedio sin usar una lista
suma = 0 # Variable para almacenar la suma de los números positivos
contador = 0 # Variable para contar la cantidad de números positivos ingresados

while True: # Bucle para solicitar al usuario que ingrese números enteros hasta que ingrese un número negativo
    numero = int(input("Ingrese un número entero (negativo para salir): ")) # Solicitar al usuario que ingrese un número entero y convertirlo a int
    if numero < 0: # Si el número ingresado es negativo, se rompe el ciclo y se procede a calcular el promedio
        break  # Salir del ciclo si el número es negativo
    suma += numero  # Sumar el número positivo a la suma total
    contador += 1  # Incrementar el contador de números positivos
if contador > 0:  # Verificar si se ingresaron números positivos
    promedio = suma / contador  # Calcular el promedio usando la suma y el contador
    print("El promedio de los números positivos ingresados es:", round(promedio, 2))
else:
    print("No se ingresaron números positivos para calcular el promedio.")

