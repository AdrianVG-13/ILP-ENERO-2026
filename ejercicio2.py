# 2. Calcular el área y perímetro de un círculo.
import math  # Importar la librería matemática para usar constantes y funciones matemáticas
# ENTRADA DE DATOS
# Declaración o creación de variables
radio = float(input("Ingresa el radio del círculo: "))  # Solicitar al usuario que ingrese el radio del círculo




# PROCESOS (Cálculos u operaciones matemáticas y/o lógicas)
área = math.pi * radio ** 2  # Cálculo del área del círculo usando la fórmula A = πr²
perímetro = 2 * math.pi * radio  # Cálculo del perímetro del círculo usando la fórmula P = 2πr



# SALIDA DE DATOS (Resultados)
print("El área del círculo es:", round(área, 2))
print("El perímetro del círculo es:", round(perímetro, 2))    
 