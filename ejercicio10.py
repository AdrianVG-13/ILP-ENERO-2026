# 10. Obtener un número y determinar lo siguiente:
# a) si es negativo y mayor a -100 imprimir los números impares de forma DESCENDENTE
# b) si es positivo y menor a 100 mostrar los números pares de forma ASCENDENTE
# c) en otro caso imprimir No Válido

# ENTRADA DE DATOS
numero = int(input("Ingrese un número: "))  

# PROCESOS (Cálculos u operaciones matemáticas y/o lógicas)
if numero < 0 and numero > -100:
    print("El número es negativo y mayor a -100. Números impares en forma descendente:")
    for i in range(-1, numero - 1, -2):  # Imprimir números impares en forma descendente
        print(i)

elif numero > 0 and numero < 100:
    print("El número es positivo y menor a 100. Números pares en forma ascendente:")
    for i in range(0, numero + 1, 2):  # Imprimir números pares en forma ascendente
        print(i)    

else:
    print("No Válido")  # Imprimir "No Válido" en cualquier otro caso



