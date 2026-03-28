
inventario = [
    {"Codigo": "P001", "Nombre": "Laptop", "Precios": 12500, "Disponibilidad": 10},
    {"Codigo": "P002", "Nombre": "Mouse", "Precios": 250, "Disponibilidad": 35},
    {"Codigo": "P003", "Nombre": "Teclado Mecánico", "Precios": 950, "Disponibilidad": 20},
    {"Codigo": "P004", "Nombre": "Monitor 24\"", "Precios": 3200, "Disponibilidad": 8},
    {"Codigo": "P005", "Nombre": "USB 32GB", "Precios": 120, "Disponibilidad": 50}
]

carrito = []

def mostrar_stock():
    try:
        print("\n📦 Inventario disponible:")
        for producto in inventario:
            print(f"Código: {producto['Codigo']} | "
                  f"Nombre: {producto['Nombre']} | "
                  f"Precio: ${producto['Precios']} | "
                  f"Stock: {producto['Disponibilidad']} piezas")
    except Exception as e:
        print(f"Error al mostrar el stock: {e}")

def agregar_al_carrito(codigo, cantidad):
    try:
        if not isinstance(codigo, str) or codigo.strip() == "":
            raise ValueError("El código debe ser una cadena no vacía.")
        cantidad_int = int(cantidad)
        if cantidad_int <= 0:
            raise ValueError("La cantidad debe ser un número entero mayor que 0.")

        for producto in inventario:
            if producto["Codigo"].upper() == codigo.strip().upper():
                if producto["Disponibilidad"] >= cantidad_int:
                    producto["Disponibilidad"] -= cantidad_int
                    # Verificar si ya estaba en el carrito
                    for item in carrito:
                        if item["Codigo"] == producto["Codigo"]:
                            item["Disponibilidad"] += cantidad_int
                            print(f"Se agregaron {cantidad_int} más de {producto['Nombre']} al carrito.")
                            return
                    carrito.append({
                        "Codigo": producto["Codigo"],
                        "Nombre": producto["Nombre"],
                        "Precios": producto["Precios"],
                        "Disponibilidad": cantidad_int
                    })
                    print(f"Se agregó {cantidad_int} {producto['Nombre']} al carrito.")
                    return
                else:
                    print(f"No hay suficiente stock de {producto['Nombre']}. Stock disponible: {producto['Disponibilidad']}")
                    return
        print("Producto no encontrado en el inventario.")
    except ValueError as ve:
        print(f"Entrada inválida: {ve}")
    except Exception as e:
        print(f"Error inesperado al agregar al carrito: {e}")

def calcular_total():
    try:
        total = sum(item["Precios"] * item["Disponibilidad"] for item in carrito)
        return total
    except Exception as e:
        print(f"Error al calcular el total: {e}")
        return 0

def menu():
    while True:
        print("\n====== Tienda - Menú ======")
        print("1. Mostrar stock")
        print("2. Agregar producto al carrito")
        print("3. Calcular total / Checkout")
        print("4. Salir")
        opcion = input("Elige una opción (1-4): ").strip()
        if opcion == "1":
            mostrar_stock()
        elif opcion == "2":
            codigo = input("Ingresa el código del producto (ej. P001): ").strip()
            cantidad = input("Ingresa la cantidad a agregar: ").strip()
            agregar_al_carrito(codigo, cantidad)
        elif opcion == "3":
            if not carrito:
                print("\n🛒 El carrito está vacío.")
            else:
                print("\n🛒 Carrito actual:")
                for item in carrito:
                    subtotal = item["Precios"] * item["Disponibilidad"]
                    print(f"{item['Nombre']} x{item['Disponibilidad']} = ${subtotal}")
                total = calcular_total()
                print(f"\n💵 Total a pagar: ${total}")
        elif opcion == "4":
            print("Saliendo... ¡nos vemos bro!")
            break
        else:
            print("Opción inválida. Elige entre 1 y 4.")

menu()
