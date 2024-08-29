from datetime import datetime, timedelta

class Paciente:
    def __init__(self, nombre_completo, edad_paciente, telefono_contacto, motivo_cita):
        self.nombre_completo = nombre_completo
        self.edad_paciente = edad_paciente
        self.telefono_contacto = telefono_contacto
        self.motivo_cita = motivo_cita
        self.estado_cita = "Pendiente"
        self.fecha_programada = None

    def programar_cita(self, dias_para_cita=2):
        self.fecha_programada = datetime.now() + timedelta(days=dias_para_cita)
        self.estado_cita = "Cita Programada"

    def mostrar_detalles(self):
        print(f"Nombre: {self.nombre_completo}")
        print(f"Edad: {self.edad_paciente}")
        print(f"Teléfono de contacto: {self.telefono_contacto}")
        print(f"Motivo de la cita: {self.motivo_cita}")
        if self.fecha_programada:
            print(f"Fecha de la cita: {self.fecha_programada.strftime('%d/%m/%Y')}")
        print(f"Estado: {self.estado_cita}")
        print("-" * 30)

def registrar_paciente():
    nombre_completo = input("¿Cuál es el nombre del paciente?: ")
    
    # Antes de continuar, revisemos si este paciente ya está registrado
    for paciente in lista_pacientes:
        if paciente.nombre_completo == nombre_completo:
            print("Este paciente ya tiene una cita agendada. Será enviado a la sala de espera.")
            paciente.estado_cita = "En sala de espera"
            return None

    # Si el paciente no está registrado, pedimos los demás datos
    edad_paciente = input("¿Cuál es la edad del paciente?: ")
    telefono_contacto = input("¿Cuál es el número de teléfono?: ")
    motivo_cita = input("¿Por qué motivo se está programando la cita?: ")
    
    nuevo_registro = Paciente(nombre_completo, edad_paciente, telefono_contacto, motivo_cita)
    nuevo_registro.programar_cita()
    return nuevo_registro

def mostrar_pacientes():
    print("\nLista de pacientes:")
    if not lista_pacientes:
        print("Aún no hay pacientes registrados.")
    else:
        for paciente in lista_pacientes:
            paciente.mostrar_detalles()

def menu_principal():
    while True:
        print("\n¿Qué te gustaría hacer?")
        print("1. Registrar un nuevo paciente")
        print("2. Ver la lista de pacientes")
        print("3. Salir del sistema")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nuevo_registro = registrar_paciente()
            if nuevo_registro:
                lista_pacientes.append(nuevo_registro)
        elif opcion == "2":
            mostrar_pacientes()
        elif opcion == "3":
            print("Cerrando el sistema...")
            break
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")

# Lista global para almacenar a todos los pacientes que se registren
lista_pacientes = []

# Ejecutamos el menú principal
menu_principal()
