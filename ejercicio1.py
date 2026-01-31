# 1.Calcular el promedio de 3 calificaciones y decir si es aprobado o reprobado.

# ENTRADA DE DATOS
# Declaración o creación de variables
calificación_1 = float(input("Ingresa la primera calificación: "))
calificación_2 = float(input("Ingresa la segunda calificación: "))
calificación_3 = float(input("Ingresa la tercera calificación: "))




# PROCESOS (Cálculos u operaciones matemáticas y/o lógicas)}
promedio = (calificación_1 + calificación_2 + calificación_3) / 3

#DETERMINAR SI APROBÓ O REPROBÓ
#if promedio >= 6.0:
    print("¡Felicidades! Has aprobado.")    
#else:
    print("Lo siento, has reprobado.")  
    


# SALIDA DE DATOS (Resultados)
print("El promedio es: ", promedio)


'''
Condicionales:
APROBADO:                   Rango (6.1 a 10)
REPROBADO:                  Rango (0 a 5.9) (0 y menor que 6.0)
APENAS APROBADO:            Equivalente (6.0)
CALIFICACIÓN INVÁLIDA       Rango (menor a 0 o mayor a 10)
'''

# Usando operaciones lógicas    
if (promedio > 6.0 and promedio <= 10.0):
    print("¡Felicidades! Has aprobado.")
elif (promedio >= 0.0 and promedio < 6.0):
    print("Lo siento, has reprobado.")
elif (promedio < 0.0 or promedio > 10.0):
    print("Calificación inválida.") 
elif (promedio == 6.0):
    print("Has aprobado apenas.")
# Nota: Se asume que la calificación máxima es 10.0 y la mínima es 0.0 para este ejemplo