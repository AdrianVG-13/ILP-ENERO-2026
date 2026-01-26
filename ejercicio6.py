# 6. Pedir un número y decir si es par o impar.
# ENTRADA DE DATOS  
numero = int(input("Ingresa un número entero: "))  # Solicitar al usuario que ingrese un número entero

# PROCESOS (Cálculos u operaciones matemáticas y/o lógicas)
if numero % 2 == 0:  # Verificar si el número es divisible por 2
    resultado = "par"  # El número es par       
else:
    resultado = "impar"  # El número es impar

# SALIDA DE DATOS (Resultados)
print("El número", numero, "es", resultado)
     