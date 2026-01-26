# 1.Calcular el promedio de 3 calificaciones y decir si es aprobado o reprobado.

# ENTRADA DE DATOS
# Declaración o creación de variables
calificación_1 = float(input("Ingresa la primera calificación: "))
calificación_2 = float(input("Ingresa la segunda calificación: "))
calificación_3 = float(input("Ingresa la tercera calificación: "))




# PROCESOS (Cálculos u operaciones matemáticas y/o lógicas)}
promedio = (calificación_1 + calificación_2 + calificación_3) / 3

#DETERMINAR SI APROBÓ O REPROBÓ
if promedio >= 6.0:
    print("¡Felicidades! Has aprobado.")    
else:
    print("Lo siento, has reprobado.")  
    


# SALIDA DE DATOS (Resultados)
print("El promedio es: ", promedio)