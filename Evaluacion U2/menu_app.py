
# Función para agregar compra
def agregar_compra(compras, total_gastado):
    print()
    monto = int(input("Ingrese el monto de la compra: "))
    compras.append(monto)
    total_gastado += monto
    print("Compra agregada correctamente.")
    print()
    input("Presione una tecla para continuar")
    return total_gastado


# Función que muestra las compras realizadas
def mostrar_compras(compras):
    print()
    if not compras:
        print("\033[91mNo hay compras registradas.\033[0m")
    else:
        for i, compra in enumerate(compras, 1):
            print(f"Compra {i}: \033[92m${compra}\033[0m")

    print()
    input("Presione una tecla para continuar")


# Función para mostrar el total gastado
def mostrar_total(total_gastado):
    print()
    print(f"Total gastado: \033[92m${total_gastado}\033[0m")
    print()
    input("Presione una tecla para continuar")


# Función MAIN
def main():
    compras = []
    total_gastado = 0

    while True:
        print("\nMenu:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            total_gastado = agregar_compra(compras, total_gastado)
        elif opcion == "2":
            mostrar_compras(compras)
        elif opcion == "3":
            mostrar_total(total_gastado)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")


main()
