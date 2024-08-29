from datetime import datetime, timedelta

class Prestamo:
    def __init__(self, nombre_usuario, titulo_libro, telefono_contacto):
        self.nombre_usuario = nombre_usuario
        self.titulo_libro = titulo_libro
        self.telefono_contacto = telefono_contacto
        self.fecha_prestamo = datetime.now()
        self.fecha_limite_devolucion = self.fecha_prestamo + timedelta(days=14)  # Plazo de 14 días para devolver el libro
        self.fecha_devolucion_real = None
        self.sancion = 0.0

    def registrar_devolucion(self, fecha_devolucion_str):
        if fecha_devolucion_str:
            self.fecha_devolucion_real = datetime.strptime(fecha_devolucion_str, "%d/%m/%Y")
        else:
            self.fecha_devolucion_real = datetime.now()

        if self.fecha_devolucion_real > self.fecha_limite_devolucion:
            dias_excedidos = (self.fecha_devolucion_real - self.fecha_limite_devolucion).days
            self.sancion = dias_excedidos * 2.0  # La sanción es de $2.00 por cada día de retraso
            print(f"El libro '{self.titulo_libro}' fue devuelto con {dias_excedidos} días de retraso. La sanción es de ${self.sancion:.2f}.")
        else:
            print(f"El libro '{self.titulo_libro}' ha sido devuelto a tiempo. No hay sanción.")

    def mostrar_detalles(self):
        print(f"Nombre del usuario: {self.nombre_usuario}")
        print(f"Libro prestado: {self.titulo_libro}")
        print(f"Teléfono de contacto: {self.telefono_contacto}")
        print(f"Fecha del préstamo: {self.fecha_prestamo.strftime('%d/%m/%Y')}")
        print(f"Fecha límite para la devolución: {self.fecha_limite_devolucion.strftime('%d/%m/%Y')}")
        if self.fecha_devolucion_real:
            print(f"Fecha de la devolución real: {self.fecha_devolucion_real.strftime('%d/%m/%Y')}")
        if self.sancion > 0:
            print(f"Sanción acumulada: ${self.sancion:.2f}")
        print("-" * 30)

def registrar_prestamo():
    nombre_usuario = input("¿Cuál es el nombre del usuario?: ")
    titulo_libro = input("¿Qué libro desea llevar en préstamo?: ")
    telefono_contacto = input("¿Cuál es el número de teléfono del usuario?: ")

    nuevo_prestamo = Prestamo(nombre_usuario, titulo_libro, telefono_contacto)
    return nuevo_prestamo

def registrar_devolucion():
    nombre_usuario = input("Ingrese el nombre del usuario que devuelve el libro: ")
    libro_a_devolver = input("Ingrese el título del libro a devolver: ")
    fecha_devolucion_str = input("Ingrese la fecha de devolución (dd/mm/yyyy) o presione Enter para usar la fecha actual: ")

    for prestamo in lista_prestamos:
        if prestamo.nombre_usuario == nombre_usuario and prestamo.titulo_libro == libro_a_devolver:
            prestamo.registrar_devolucion(fecha_devolucion_str)
            return

    print("No se encontró el préstamo con los datos proporcionados.")

def mostrar_prestamos():
    print("\nPréstamos registrados:")
    if not lista_prestamos:
        print("No hay préstamos registrados.")
    else:
        for prestamo in lista_prestamos:
            prestamo.mostrar_detalles()

def menu_principal():
    while True:
        print("\n¿Qué te gustaría hacer?")
        print("1. Registrar un nuevo préstamo")
        print("2. Registrar la devolución de un libro")
        print("3. Ver la lista de préstamos")
        print("4. Salir del sistema")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nuevo_prestamo = registrar_prestamo()
            lista_prestamos.append(nuevo_prestamo)
        elif opcion == "2":
            registrar_devolucion()
        elif opcion == "3":
            mostrar_prestamos()
        elif opcion == "4":
            print("Cerrando el sistema...")
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

# Lista global para almacenar los préstamos registrados
lista_prestamos = []

# Ejecutamos el menú principal
menu_principal()
