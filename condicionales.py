# Condicionales. Mayoría de edad

# ENTRADAS DE DATOS
edad = int(input("Escribe tu edad: "))  # Solicitar al usuario que ingrese su edad

# PROCESOS Y CONDICIONALES
if (edad >= 18):  # Verificar si la edad es mayor o igual a 18
    print("Mayor de edad")  # Mostrar mensaje si es mayor de edad
elif (edad <18): # Verificar si la edad es menor a 18
    
# SALIDAS DE DATOS
    print("Menor de edad")  # Mostrar mensaje si es menor de edad

# oTRA FORMA DE HACERLO, en este caso no se utilizo elif ya que else cubre todas las demás opciones
# if (edad >= 18):
#     print("Mayor de edad")    
# else:
#     print("Menor de edad")    

# Usando peraciones lógicas
if (edad >= 18 and edad <= 110):  # Verificar si la edad está entre 18 y 110 años
    print("Mayor de edad")  # Mostrar mensaje si es mayor de edad
elif: (edad >= 0 and edad < 18):           # Rango valido (0 y 17)
    print("Menor de edad")  # Mostrar mensaje si es menor de edad
else: 
    print("Edad no válida")  # Mostrar mensaje si la edad no es válida, ya sea menor a 0 o mayor a 110

# En lugar de else se puede usar otro elif para validar un rango específico
#elif (edad < 0 or edad > 110):  # Verificar si la edad es menor a 0 o mayor a 110
#   print("Edad no válida")  # Mostrar mensaje si la edad no es válida
# Cuando se coloca == en lugar de >= o <= se está preguntando si es exactamente igual a ese valor
# Nota: Se asume que la edad máxima es 110 años para este ejemplo



