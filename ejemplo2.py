#Operaciones Matemáticas Básicas

# ENTRADAS DE DATOS
# Declaración o creación de variables
número_1 = float(input("Ingresa el primer número: ")) # Solicitar al usuario que ingrese el primer número
número_2 = float(input("Ingresa el segundo número: ")) # Solicitar al usuario que ingrese el segundo número

# PROCESOS (Cáslculos u operaciones matemáticas y/o lógicas)
suma = número_1 + número_2
resta = número_1 - número_2
multiplicación = número_1 * número_2
división = número_1 / número_2  
potencia = número_1 ** número_2 # Primer número elevado a la potencia del segundo número
raiz_cuadrada = número_1 ** 0.5  # Raíz cuadrada del primer número
raiz_cúbica = número_1 ** (1/3)  # Raíz cúbica del primer número
módulo = número_1 % número_2  # Resto de la división entre el primer y segundo número

# SALIDAS DE DATOS (Resultados)
print("Suma =", suma) #Mostrar resultado de la suma
print("Resta =", resta) #Mostrar resultado de la resta
print("Multiplicación =" + str(multiplicación)) # CONCATENACIÓN con (Conversión de un tipo de dato en otro dato) Mostrar resultado de la multiplicación
print(f"División = {división}") # Interpolación de cadenas, Mostrar resultado de la división usando f-string
print("Potencia =", potencia) #Mostrar resultado de la potencia
print("Raíz Cuadrada =", raiz_cuadrada) #Mostrar resultado de la raíz cuadrada
print("Raíz Cúbica =", raiz_cúbica) #Mostrar resultado de
print("Módulo =", módulo) #Mostrar resultado del módulo

# COMENTAR CTRL + K + C
# DESCOMENTAR CTRL + K + U
