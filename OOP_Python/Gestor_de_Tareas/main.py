
class Tarea:
    def __init__(self, descripcion, completada=False):
        self.description = descripcion
        self.completada = completada

    def completar(self):
        self.completada = True

    def descompletar(self):
        self.completada = False

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"Tarea: {self.description} ({estado})"

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tara(self, descripcion):
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)

    def listar_tareas(self):
        if self.tareas:
            for index, tarea in enumerate(self.tareas, start=1):
                print(f"{index}: {tarea}")
        else:
            print("No hay tareas pendientes.")

    def completar_tarea(self, numero_tarea):
        if 1 <= numero_tarea <= len(self.tareas):
            self.tareas[numero_tarea - 1].completar()
            print(f"Tarea {numero_tarea} completada.")
        else:
            print("Numero de tarea invalido.")

    def descompletar_tarea(self, numero_tarea):
        if 1 <= numero_tarea <=len(self.tareas):
            self.tareas[numero_tarea - 1].descompletar()
            print(f"Tarea {numero_tarea} marcada como pendiente.")
        else:
            print("Número de tarea inválido.")

    def eliminar_tarea(self, numero_tarea):
        if 1 <= numero_tarea <= len(self.tareas):
            tarea_eliminada = self.tareas.pop(numero_tarea - 1)
            print(f"Tarea {numero_tarea}: {tarea_eliminada.descripcion} ")
        else:
            print("Número de tarea inválido.")


def main():
    gestor = GestorTareas()

    while True:
        print("Opciones:\n1. Agregar Tarea\n2. Listar Tareas\n3. Completar Tarea\n4. Descompletar Tarea\n5. Eliminar "
              "Tarea\n6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            descripcion = input("Ingrese la descripción de la tarea: ")
            gestor.agregar_tara(descripcion)
        elif opcion == "2":
            gestor.listar_tareas()
        elif opcion == "3":
            num_tarea = int(input("Ingresa el número de la tarea a completar: "))
            gestor.completar_tarea(num_tarea)
        elif opcion == "4":
            num_tarea = int(input("Ingresa el número de la tarea a descompletar: "))
            gestor.descompletar_tarea(num_tarea)
        elif opcion == "5":
            num_tarea = int(input("Ingresa el número de la tarea a eliminar: "))
            gestor.eliminar_tarea(num_tarea)
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()