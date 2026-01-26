#Operaciones Matemáticas Básicas

# Importación de Librerias: Mandar a llamar archivos de Python para usar funciones y constantes específicas
import math  # Librería matemática para funciones avanzadas (opcional)
from colorama import Fore, Style  # Librería para colores en la consola (opcional)

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
potencia2 = pow(número_1, número_2)  # Otra forma de calcular la potencia usando la función pow()
cuadrado = número_1 ** 2  # Cuadrado del primer número
cubo = número_1 ** 3  # Cubo del primer número
raiz_cuadrada = número_1 ** 0.5  # Raíz cuadrada del primer número
raíz_cuadrada2 = math.sqrt(número_1)  # Otra forma de calcular la raíz cuadrada usando la función sqrt() de la librería math
raiz_cuadrada3 = pow(número_1, 0.5)  # Otra forma de calcular la raíz cuadrada usando la función pow()
raiz_cúbica = número_1 ** (1/3)  # Raíz cúbica del primer número
raíz_cúbica2 = pow(número_1, 1/3)  # Otra forma de calcular la raíz cúbica usando la función pow()
módulo = número_1 % número_2  # Resto de la división entre el primer y segundo número
módulo2 = divmod(número_1, número_2)[1]  # Otra forma de calcular el módulo usando la función divmod()

# SALIDAS DE DATOS (Resultados)
print(Fore.GREEN + "Suma =", suma) #Mostrar resultado de la suma
print(Fore.RED + "Resta = ", resta, Style.RESET_ALL) #Mostrar resultado de la resta
print("Multiplicación =" + str(multiplicación)) # CONCATENACIÓN con (Conversión de un tipo de dato en otro dato) Mostrar resultado de la multiplicación
print(f"División = {división}") # Interpolación de cadenas, Mostrar resultado de la división usando f-string
print("Potencia =", potencia) #Mostrar resultado de la potencia
print("Raíz Cuadrada =", raiz_cuadrada) #Mostrar resultado de la raíz cuadrada
print("Raíz Cúbica =", raiz_cúbica) #Mostrar resultado de
print("Módulo =", módulo) #Mostrar resultado del módulo

# COMENTAR CTRL + K + C
# DESCOMENTAR CTRL + K + U
