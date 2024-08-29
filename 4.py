class Vehiculo:
    def __init__(self, tipo, marca, modelo, precio_dia):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.precio_dia = precio_dia

    def calcular_costo_renta(self, dias):
        return self.precio_dia * dias

    def mostrar_info(self):
        print(f"Tipo de Vehículo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Precio por Día: ${self.precio_dia:.2f}")
        print("-" * 30)

# Lista global para almacenar los vehículos
vehiculos_disponibles = []

def registrar_vehiculo():
    print("Ingrese los datos del nuevo vehículo:")
    tipo = input("Tipo de vehículo (Ej. Auto, Moto, Camión): ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    precio_dia = float(input("Precio por día: "))
    
    vehiculo = Vehiculo(tipo=tipo, marca=marca, modelo=modelo, precio_dia=precio_dia)
    vehiculos_disponibles.append(vehiculo)
    print("Vehículo registrado exitosamente.")
    print("-" * 30)

def listar_vehiculos():
    if not vehiculos_disponibles:
        print("No hay vehículos disponibles en este momento.")
    else:
        print("Vehículos disponibles para renta:")
        for idx, vehiculo in enumerate(vehiculos_disponibles):
            print(f"\nVehículo {idx + 1}:")
            vehiculo.mostrar_info()

def rentar_vehiculo():
    listar_vehiculos()
    
    if not vehiculos_disponibles:
        return
    
    try:
        seleccion = int(input("Ingrese el número del vehículo que desea rentar: ")) - 1
        if seleccion < 0 or seleccion >= len(vehiculos_disponibles):
            print("Selección inválida. Intente de nuevo.")
            return rentar_vehiculo()

        vehiculo = vehiculos_disponibles[seleccion]
        dias = int(input("Ingrese el número de días de renta: "))
        cliente = input("Ingrese el nombre del cliente: ")
        
        costo_total = vehiculo.calcular_costo_renta(dias)
        
        print("\nDetalles de la renta:")
        print(f"Cliente: {cliente}")
        vehiculo.mostrar_info()
        print(f"Días de Renta: {dias}")
        print(f"Costo Total de Renta: ${costo_total:.2f}")
        print("-" * 30)
    
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")
        return rentar_vehiculo()

def menu_principal():
    while True:
        print("Seleccione la opción que desea realizar:")
        print("1. Registrar nuevo vehículo")
        print("2. Listar vehículos disponibles")
        print("3. Rentar vehículo")
        print("4. Salir")
        
        try:
            opcion = int(input("Ingrese el número correspondiente a la opción que desea realizar: "))
            
            if opcion == 1:
                registrar_vehiculo()
            elif opcion == 2:
                listar_vehiculos()
            elif opcion == 3:
                rentar_vehiculo()
            elif opcion == 4:
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
        
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

menu_principal()
