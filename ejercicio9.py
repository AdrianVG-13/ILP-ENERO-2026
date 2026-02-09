# 9.- Realizar un Menú de Opciones y realizar una función para cada opción:
#******** MENÚ *********
#a) Mostrar una lista de 3 servicios de entrega de pedidos con sus estrellas de calificación
#b) Generar una contraseña con el número de caracteres pedidos menor o igual a 5, si es mayor que 5 mostrar mensaje de error
#c) Pedir al usuario su nombre, primer ap., segundo ap. y edad e imprimir un saludo con sus datos

# import secrets  # Importar la librería secrets para generar contraseñas seguras (opcional)
# import string  # Importar la librería string para usar caracteres predefinidos (opcional)

# Variable global para almacenar el nombre del usuario
usuario_nombre = None

def mostrar_servicios():
    servicios = [
        ("Uber Eats", "⭐⭐⭐⭐⭐"),
        ("Rappi", "⭐⭐⭐⭐☆"),
        ("Didi Food", "⭐⭐⭐☆☆")
    ]
    print("\n--- Servicios de entrega ---")
    for nombre, estrellas in servicios:
        print(f"{nombre}: {estrellas}")

# Función para generar contraseña
def generar_contrasena():
    longitud = int(input("Ingrese el número de caracteres de la contraseña: "))
    if longitud <= 5:
        import random
        import string
        caracteres = string.ascii_letters + string.digits
        contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
        print(f"Contraseña generada: {contrasena}")
    else:
        print("Error: la longitud debe ser menor o igual a 5.")

# Función para pedir datos del usuario
def pedir_datos():
    global usuario_nombre # Se usará la variable global para almacenar el nombre del usuario
    nombre = input("Ingrese su nombre: ")
    primer_ap = input("Ingrese su primer apellido: ")
    segundo_ap = input("Ingrese su segundo apellido: ")
    edad = input("Ingrese su edad: ")
    usuario_nombre = nombre # Variable para almacenar el nombre del usuario
    print(f"\nHola {nombre} {primer_ap} {segundo_ap}, tienes {edad} años. ¡Bienvenido!")

# Menú principal
def menu():
    while True:
        print("\n******** MENÚ *********")
        print("a) Mostrar servicios de entrega")
        print("b) Generar contraseña")
        print("c) Pedir datos y saludar")
        print("d) Salir")

        opcion = input("Seleccione una opción: ").lower()

        if opcion == "a":
            mostrar_servicios()
        elif opcion == "b":
            generar_contrasena()
        elif opcion == "c":
            pedir_datos()
        elif opcion == "d":
            if usuario_nombre: # Verificar si el usuario ha ingresado su nombre antes de mostrar el mensaje de despedida
                print(f"Saliendo del programa, hasta pronto {usuario_nombre}...")

            else:
                print(f"Saliendo del programa, hasta pronto ...")
            break

        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar menú
menu()

