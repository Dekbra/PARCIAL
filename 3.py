class Habitacion:
    def __init__(self, tipo, precio_noche):
        self.tipo = tipo
        self.precio_noche = precio_noche

    def calcular_costo_estadia(self, noches):
        return self.precio_noche * noches

    def mostrar_info(self):
        print(f"Tipo de Habitación: {self.tipo}")
        print(f"Precio por Noche: ${self.precio_noche:.2f}")
        print("-" * 30)

def ingresar_habitacion():
    print("Seleccione el tipo de habitación que desea registrar:")
    print("1. Suite")
    print("2. Doble")
    print("3. Sencilla")
    opcion = int(input("Ingrese el número correspondiente al tipo de habitación: "))

    if opcion == 1:
        tipo = "Suite"
        precio_noche = float(input("Ingrese el precio por noche para la Suite: "))
    elif opcion == 2:
        tipo = "Doble"
        precio_noche = float(input("Ingrese el precio por noche para la habitación Doble: "))
    elif opcion == 3:
        tipo = "Sencilla"
        precio_noche = float(input("Ingrese el precio por noche para la habitación Sencilla: "))
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
        return ingresar_habitacion()

    return Habitacion(tipo=tipo, precio_noche=precio_noche)

def servicios_extra():
    print("Seleccione los servicios adicionales que desea agregar:")
    print("1. Uso de la piscina - $50 por noche")
    print("2. Acceso a la cancha de golf - $100 por noche")
    print("3. Ninguno")

    opcion = int(input("Ingrese el número correspondiente al servicio adicional: "))

    if opcion == 1:
        return 50
    elif opcion == 2:
        return 100
    elif opcion == 3:
        return 0
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
        return servicios_extra()

def registrar_estadia():
    habitacion = ingresar_habitacion()
    noches = int(input("Ingrese el número de noches de estadía: "))
    cliente = input("Ingrese el nombre del cliente: ")
    
    costo_estadia = habitacion.calcular_costo_estadia(noches)
    costo_servicios = servicios_extra() * noches
    
    print("\nDetalles de la estadía:")
    print(f"Cliente: {cliente}")
    habitacion.mostrar_info()
    print(f"Noches de Estadía: {noches}")
    print(f"Costo Total de Estadía: ${costo_estadia:.2f}")
    if costo_servicios > 0:
        print(f"Costo Total de Servicios Adicionales: ${costo_servicios:.2f}")
    print(f"Costo Total a Pagar: ${costo_estadia + costo_servicios:.2f}")
    print("-" * 30)

def menu_principal():
    while True:
        print("Seleccione la opción que desea realizar:")
        print("1. Registrar estadía de cliente")
        print("2. Salir")
        opcion = int(input("Ingrese el número correspondiente a la opción que desea realizar: "))

        if opcion == 1:
            registrar_estadia()
        elif opcion == 2:
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

menu_principal()
