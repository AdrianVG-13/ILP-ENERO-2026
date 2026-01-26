# Obtener valores para: a, b y c. Calcular la fórmula general
import math
# ENTRADA DE DATOS
# Declaración o creación de variables

a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))     
C = float(input("Ingresa el valor de c: "))
    

# PROCESOS (Cálculos u operaciones matemáticas y/o lógicas)
discriminante = b**2 - 4*a*C
if discriminante < 0:
    print("No existen soluciones reales.")      
else:
    raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
    raiz2 = (-b - math.sqrt(discriminante)) / (2*a)     
 

# SALIDA DE DATOS (Resultados)
    print("Las soluciones son:")
    print("Raíz 1:", round(raiz1, 2))
    print("Raíz 2:", round(raiz2, 2))   
    

