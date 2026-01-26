# 4. Pedir la cantidad de grados y convertirlos a °C, °F y K.

# ENTRADA DE DATOS
# Declaración o creación de variables 
grados = float(input("Ingresa la cantidad de grados: "))  # Solicitar al usuario que ingrese la cantidad de grados en Celsius    
# PROCESOS (Cálculos u operaciones matemáticas y/o lógicas)
grados_celsius = (grados - 273.15)  # Grados en Celsius (°C)
grados_fahrenheit = (grados * 9/5) + 32  # Conversión de °C a °F usando la fórmula F = (C * 9/5) + 32
grados_kelvin = grados  + 273.15  # Conversión de °C a K usando la fórmula K = C + 273.15
# SALIDA DE DATOS (Resultados)  
print("Grados en Celsius:", round(grados_celsius, 2))
print("Grados en Fahrenheit:", round(grados_fahrenheit, 2))
print("Grados en Kelvin:", round(grados_kelvin, 2))