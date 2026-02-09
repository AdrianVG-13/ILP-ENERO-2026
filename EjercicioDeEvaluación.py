# Realizar un programa que realice un cuestionario con las siguientes 12 preguntas, muestre su resultado aciertos / 12 y mostrar la calificación = (aciertos / 12) * 10:
from colorama import Fore, Style, init  # Librería para colores en la consola
init(autoreset=True)  # Inicializar colorama para restablecer colores automáticamente después de cada impresión
aciertos = 0 # Variable para contar el número de respuestas correctas
print("1. Herramienta de programación, parecido al lenguaje español utilizado para crear código.\n     a) IDE     b) Pseudocódigo     c) Compilador     d) ANSI/ISO")
respuesta1 = input("Selecciona tu respuesta: ")
if(respuesta1 == "b"):
    print(Fore.GREEN + "¡Respuesta correcta!")
    aciertos = aciertos + 1 # Se incrementa el contador de aciertos en 1
else:
    print(Fore.RED + "Respuesta incorrecta.")  

print("2.  Conjunto de símbolos, letras, números, imágenes, audio y video organizadas y que son relevantes en un tiempo y forma determinados.\n     a) Información     b) Datos     c) Programa    d) Código ")
respuesta2 = input("Selecciona tu respuesta: ")
if(respuesta2 == "a"):
    print(Fore.GREEN + "¡Respuesta correcta!")
    aciertos = aciertos + 1 # Se incrementa el contador de aciertos en 1    
else:
    print(Fore.RED + "Respuesta incorrecta.")

print("3.Instituciones encargadas de estandarizar reglas y simbología de los Diagramas de Flujo.\n     a) IEEE     b) IDE     c) ANSI/ISO     d) VSCode")
respuesta3 = input("Selecciona tu respuesta: ")
if(respuesta3 == "c"):
    print(Fore.GREEN +  "¡Respuesta correcta!")
    aciertos = aciertos + 1 # Se incrementa el contador de aciertos en 1
else:
    print(Fore.RED + "Respuesta incorrecta.")

print("4.Serie de pasos consecutivos, ordenados y finitos que se siguen para resolver un problema.\n     a) Proceso     b) Solución     c) Función     d) Algoritmo")
respuesta4 = input("Selecciona tu respuesta: ")
if(respuesta4 == "d"):
    print(Fore.GREEN + "¡Respuesta correcta!")
    aciertos = aciertos + 1 # Se incrementa el contador de aciertos en 1
else:
    print(Fore.RED + "Respuesta incorrecta.")

print("5.Conjunto de elementos que se relacionan para cumplir una función determinada.\n     a) Estructura     b) Datos     c) Operación     d) Sistema")
respuesta5 = input("Selecciona tu respuesta: ")
if(respuesta5 == "d"):
    print(Fore.GREEN + "¡Respuesta correcta!")
    aciertos = aciertos + 1 # Se incrementa el contador de aciertos en 1    
else:
    print(Fore.RED + "Respuesta incorrecta.")

print("6. Componente de un IDE que se encarga de traducir el código fuente a código máquina.\n     a) Depurador     b) Editor de Texto     c) Terminal de Salida     d) Compilador/Intérprete")  
respuesta6 = input("Selecciona tu respuesta: ")
if(respuesta6 == "d"):
    print(Fore.GREEN + "¡Respuesta correcta!")
    aciertos = aciertos + 1 # Se incrementa el contador de aciertos en 1
else:
    print(Fore.RED + "Respuesta incorrecta.")

print("7. Elemento que se usa para almacenar una cantidad donde cambia su valor.\n     a) Constante     b) Variable     c) Librería     d) Tipo de Dato")
respuesta7 = input("Selecciona tu respuesta: ")
if(respuesta7 == "b"):
    print(Fore.GREEN + "¡Respuesta correcta!")
    aciertos = aciertos + 1 # Se incrementa el contador de aciertos en 1
else:
    print(Fore.RED + "Respuesta incorrecta.")

print("8. Conjunto de símbolos, letras, números que no tienen un significado.\n     a) Datos     b) Estructura     c) Información     d) Sistema ")
respuesta8 = input("Selecciona tu respuesta: ")
if(respuesta8 == "a"):
    print(Fore.GREEN + "¡Respuesta correcta!")
    aciertos = aciertos + 1 # Se incrementa el contador de aciertos en 1    
else:
    print(Fore.RED + "Respuesta incorrecta.")

print("9. Disciplina que argumenta conclusiones a partir de premisas mediante un razonamiento.\n     a) Filosofía     b) Sociología     c) Lógica     d) Argumentación")
respuesta9 = input("Selecciona tu respuesta: ")
if(respuesta9 == "c"):
    print(Fore.GREEN + "¡Respuesta correcta!")
    aciertos = aciertos + 1 # Se incrementa el contador de aciertos en 1    
else:
    print(Fore.RED + "Respuesta incorrecta.")

print("10. Medida, patrón, modelo o norma universal para realizar una actividad o producir un objeto.\n     a) Evento     b) Estándar     c) Calidad     d) Productividad")
respuesta10 = input("Selecciona tu respuesta: ")
if(respuesta10 == "b"):
    print(Fore.GREEN + "¡Respuesta correcta!")
    aciertos = aciertos + 1 # Se incrementa el contador de aciertos en 1    
else:
    print(Fore.RED + "Respuesta incorrecta.")

print("11. Conjunto de elementos ordenados que componen y son la base de algo físico o no físico.\n     a) Estructura     b) Sistema     c) Objeto     d) Virtual")
respuesta11 = input("Selecciona tu respuesta: ")
if(respuesta11 == "a"):
    print(Fore.GREEN + "¡Respuesta correcta!")
    aciertos = aciertos + 1 # Se incrementa el contador de aciertos en 1    
else:
    print(Fore.RED + "Respuesta incorrecta.")

print("12. Conjunto de instrucciones (código) que indican a la computadora tareas a realizar.\n     a) Operaciones/Cálculos     b) Sintaxis     c) Programa de Computadora     d) Comando ")
respuesta12 = input("Selecciona tu respuesta: ")
if(respuesta12 == "c"):
    print(Fore.GREEN + "¡Respuesta correcta!")
    aciertos = aciertos + 1 # Se incrementa el contador de aciertos en 1
else:
    print(Fore.RED + "Respuesta incorrecta.")

print("El número de aciertos es: ", aciertos)
calificación = (aciertos / 12) * 10
print("Tu calificación es: ", round(calificación, 2))