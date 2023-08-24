def main_menu():
    print("Bienvenido al sistema de control de versiones.")
    print("1. Crear nueva versión")
    print("2. Mostrar versión actual")
    print("3. Salir")

    choice = input("Seleccione una opción: ")

    if choice == "1":
        crear_nueva_version()
    elif choice == "2":
        mostrar_version_actual()
    elif choice == "3":
        print("Saliendo del programa.")
        exit()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

def crear_nueva_version():
    # Aquí iría el código para crear una nueva versión
    print("Nueva versión creada exitosamente.")

def mostrar_version_actual():
    # Aquí iría el código para mostrar la versión actual
    print("Versión actual: 1.0")

if __name__ == "__main__":
    while True:
        main_menu()
