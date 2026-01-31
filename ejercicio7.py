# 7. Pedir el nivel del agua en metros de una cisterna

# ENTRADA DE DATOS
# Declaración o creación de variables
nivel_agua = float(input("Ingresa el nivel del agua en metros: "))

# PROCESOS (Cálculos u operaciones matemáticas y/o lógicas)
if nivel_agua > 6:
    print("Desbordamiento de Agua en Cisterna")
elif nivel_agua == 6:
    print("Apagar Bomba de Agua")
elif nivel_agua >=4 and nivel_agua < 6:
    print("Desacelerar Bomba de Agua")
elif nivel_agua >=2 and nivel_agua < 4:
    print("Bomba de Agua trabajando!")
elif nivel_agua >0 and nivel_agua < 2:
    print("Acelerar Bomba de Agua")
elif nivel_agua ==  0:
    print("Encender Bomba de Agua")
elif nivel_agua < 0:
    print("Fuga de Cisterna")
