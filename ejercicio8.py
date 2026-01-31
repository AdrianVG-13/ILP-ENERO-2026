# 8. Calcular la nómina para un empleado en el mes de Enero del 2026, preguntanlo su pago por día y conociendo las siguientes deducciones
# ENTRADA DE DATOS
# Declaración o creación de variables
IVA_retenido = 0.16  # Tasa de IVA retenido (16%)
ISR_retenido = 0.10  # Tasa de ISR retenido (10%)
# Solicitar al usuario que ingrese el número de días laborables en enero del 2026
días_laborables = int(input("Ingresa el número de días laborables en enero del 2026: "))
pago_por_día = float(input("Ingresa el pago por día del empleado: "))

# PROCESOS (Cálculos u operaciones matemáticas y/o lógicas)
nómina_bruta = pago_por_día * días_laborables  # Cálculo de la nómina bruta del empleado
IVA_Trasladado = nómina_bruta * 0.16  # Cálculo del IVA trasladado (16%)
Subtotal = nómina_bruta + IVA_Trasladado  # Cálculo del subtotal con IVA trasladado
IVA = 2/3 * IVA_Trasladado # Cálculo del IVA retenido   
ISR = nómina_bruta * 0.10  # Cálculo del ISR retenido   
nómina_mensual = Subtotal - IVA - ISR  # Cálculo de la nómina mensual   

# SALIDA DE DATOS (Resultados)
print(f"La nómina bruta del empleado es: ${nómina_bruta}")  
print(f"El IVA trasladado es: ${IVA_Trasladado}")  
print(f"El subtotal con IVA trasladado es: ${Subtotal}")
print(f"El IVA retenido es: ${IVA}")    
print(f"El ISR retenido es: ${ISR}")    
print(f"La nómina mensual del empleado es: ${nómina_mensual}")  
