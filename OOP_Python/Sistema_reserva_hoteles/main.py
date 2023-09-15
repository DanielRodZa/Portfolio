from habitaciones import habitaciones_data

class GestorHabitaciones:
    def __init__(self):
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def listar_habitaciones_disponibles(self):
        habitaciones_disponibles = [habitacion for habitacion in self.habitaciones if habitacion.disponible]
        if habitaciones_disponibles:
            print("Habitaciones Disponibles:")
            for habitacion in habitaciones_disponibles:
                print(habitacion)
        else:
            print("No hay habitaciones disponibles en este momento.")

class HabitacionHotel:
    def __init__(self, numero, tipo, capacidad, precio_noche, disponible=True):
        self.numero = numero
        self.tipo = tipo
        self.capacidad = capacidad
        self.precio_noche = precio_noche
        self.disponible = disponible

    def reservar(self):
        if self.disponible:
            self.disponible = False
            return "La habitación ha sido reservada exitosamente."
        else:
            return "Lo siento, la habitación no está disponible en este momento."

    def liberar_habitacion(self):
        if not self.disponible:
            self.disponible = True
            return "La habitación ha sido liberada."
        else:
            return "La habitación ya está disponible."

    def __str__(self):
        disponibilidad = "Disponible" if self.disponible else "No disponible"
        return (f"Habitación {self.numero}: Tipo {self.tipo}, Capacidad {self.capacidad}, Precio"
                f" por noche ${self.precio_noche}, {disponibilidad}")

class Reserva:
    def __init__(self, cliente, habitacion, noches):
        self.cliente = cliente
        self.habitacion = habitacion
        self.noches = noches
        self.total = habitacion.precio_noche * noches

    def __str__(self):
        return f"Reserva para {self.cliente}: {self.habitacion}, {self.noches} noches, Total: ${self.total}"

class Menu:
    def __init__(self, gestor_habitaciones):
        self.gestor_habitaciones = gestor_habitaciones

    def mostrar_menu(self):
        while True:
            print("\n¿Qué deseas hacer?")
            print("1. Reservar")
            print("2. Liberar")
            print("3. Listar habitaciones disponibles")
            print("4. Salir")

            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.reservar_habitacion()
            elif opcion == "2":
                self.liberar_habitacion()
            elif opcion == "3":
                self.listar_habitaciones_disponibles()
            elif opcion == "4":
                print("Hasta luego.")
                break
            else:
                print("Por favor, introduce una opción válida.")

    def reservar_habitacion(self):
        cliente = input("Nombre del cliente: ")
        habitacion = int(input("¿Qué habitación deseas reservar? "))
        noches = int(input("¿Cuántas noches reserva? "))
        reserva = Reserva(cliente, self.gestor_habitaciones.habitaciones[habitacion - 1], noches)
        print(reserva)
        print(self.gestor_habitaciones.habitaciones[habitacion - 1].reservar())

    def liberar_habitacion(self):
        habitacion = int(input("¿Qué habitación deseas liberar? "))
        print(self.gestor_habitaciones.habitaciones[habitacion - 1].liberar_habitacion())

    def listar_habitaciones_disponibles(self):
        self.gestor_habitaciones.listar_habitaciones_disponibles()

def main():
    gestor_habitaciones = GestorHabitaciones()

    habitaciones = [HabitacionHotel(**data) for data in habitaciones_data]

    for habitacion in habitaciones:
        gestor_habitaciones.agregar_habitacion(habitacion)

    menu = Menu(gestor_habitaciones)

    menu.mostrar_menu()

if __name__ == "__main__":
    main()
