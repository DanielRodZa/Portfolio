import csv
import os
import glob
import datetime


# TODO: verificar que el saldo lo tome del csv


class Cuenta:
    """
    Esta clase representa una cuenta bancaria, de crédito o débito.

    Atributos:
        nombre (str): Nombre de la cuenta (banco, crédito, débito).
        saldo (float): Saldo actual de la cuenta.
        movimientos (list): Lista de movimientos (ingresos y gastos).

    Métodos:
        registrar_movimiento(fecha, descripcion, monto): Registra un nuevo movimiento en la cuenta.
        consultar_saldo(): Consulta el saldo actual de la cuenta.
        generar_estado_cuenta(fecha_inicio, fecha_fin): Genera un estado de cuenta detallado por fechas.
    """

    def __init__(self, nombre):
        self.nombre = nombre
        self.saldo = self.actualizar_saldo()
        self.movimientos = []

        ruta_archivo = f'{self.nombre}.csv'
        if os.path.isfile(ruta_archivo):
            with open(ruta_archivo, 'r') as archivo:
                lector = csv.reader(archivo)
                next(lector)
                for fila in lector:
                    fecha, hora, descripcion, monto = fila
                    movimiento = [fecha, hora, descripcion, monto]
                    if movimiento[3] != '':
                        self.movimientos.append(movimiento)
                        self.saldo += float(movimiento[3])

    def menu_cuenta(self):
        """
        Este método presenta el menú de opciones para realizar operaciones sobre la cuenta
        """
        while True:
            print(f'\nMenú cuenta - {self.nombre}')
            print('1. Registrar movimiento')
            print('2. Consultar saldo')
            print('3. Generar estado de cuenta')
            print('4. Volver al menú principal')

            opcion = int(input('Ingrese una opción: '))
            if opcion == 1:
                fecha = input('Ingrese la fecha del movimiento (dd/mm/aaaa): ')
                descripcion = input('Ingrese la descripcion del movimiento: ')
                monto = float(input('Ingrese el monto del movimiento: '))
                self.registrar_movimiento(fecha=fecha, descripcion=descripcion, monto=monto)
                print('Movimiento registrado exitosamente!')
            elif opcion == 2:
                saldo = self.consultar_saldo()
                print(f'Saldo actual de la cuenta {self.nombre}: {saldo}')
            elif opcion == 3:
                fecha_inicio = input('Ingrese la fecha de inicio (dd/mm/aaaa): ')
                fecha_fin = input('Ingrese la fecha fianl (dd/mm/aaaa): ')
                self.generar_estado_cuenta(fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)
            elif opcion == 4:
                print('Regreando al menu principal...')
                break
            else:
                print('Opcion inválida. Intente nuevamente...')

    def registrar_movimiento(self, fecha, descripcion, monto):
        """
        Registra un nuevo movimiento (ingreso o gasto) en la cuenta.

        Parámetros:
            fecha (str): Fecha del movimiento (formato dd/mm/aaaa).
            descripcion (str): Descripción del movimiento.
            monto (float): Monto del movimiento.
        """
        hora = datetime.datetime.now()
        hora_formateada = hora.strftime("%H:%M")
        movimiento = [fecha, hora_formateada, descripcion, monto]
        with open(f'{self.nombre}.csv', 'a', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(movimiento)
        self.movimientos.append(movimiento)
        self.saldo += monto

    def consultar_saldo(self):
        """
        Consulta el saldo actual de la cuenta.

        Returns:
            float: Saldo actual de la cuenta.
        """
        saldo = self.actualizar_saldo()
        return saldo

    def generar_estado_cuenta(self, fecha_inicio, fecha_fin):
        """
        Genera un estado de cuenta detallado por fechas para la cuenta.

        Args:
            fecha_inicio (str): Fecha inicial del estado de cuenta (formato dd/mm/aaaa).
            fecha_fin (str): Fecha final del estado de cuenta (formato dd/mm/aaaa).

        Returns:
            None
        """
        print(f'Generando estado de cuenta {self.nombre}')
        print(f'Fecha inicio: {fecha_inicio} - Fecha final: {fecha_fin}')

        saldo_incial = self.saldo
        print(f'Saldo incial: {saldo_incial}')

        movimientos_filtrados = [m for m in self.movimientos if fecha_inicio <= m[0] <= fecha_fin]
        for movimiento in movimientos_filtrados:
            fecha, hora, descripcion, monto = movimiento
            print(f'{fecha}/{hora} - {descripcion}: {monto}')

        saldo_final = saldo_incial + sum(float(m[2]) for m in movimientos_filtrados)
        print(f'Saldo final: {saldo_final}')

    def actualizar_saldo(self):
        saldo = 0.0
        ruta_archivo = f'{self.nombre}.csv'
        if os.path.isfile(ruta_archivo):
            with open(ruta_archivo, 'r') as archivo:
                lector = csv.reader(archivo)
                next(lector)
                for fila in lector:
                    fecha, hora, descripcion, monto = fila
                    movimiento = [fecha, hora, descripcion, monto]
                    # self.movimientos.append(movimiento)
                    if fecha != '':
                        saldo += float(movimiento[3])
        return saldo



def listar_cuentas():
    archivos_csv = glob.glob('*.csv')
    cuentas = [Cuenta(os.path.splitext(archivo)[0]) for archivo in archivos_csv]
    return cuentas


def imprimir_cuentas(cuentas):
    if not cuentas:
        print('No hay cuentas registradas.')
    else:
        print('\nCuentas disponibles:')
        for i, cuenta in enumerate(cuentas):
            print(f'{i + 1}. {cuenta.nombre}')


def seleccionar_cuenta(cuentas):
    if not cuentas:
        print('No hay cuentas registradas.')
    else:
        print('\nCuentas disponibles:')
        imprimir_cuentas(cuentas)
        seleccion = int(input('Seleccione una de las cuentas disponibles:\n'))
        if 0 <= seleccion < len(cuentas) + 1:
            cuentas[seleccion - 1].menu_cuenta()
        else:
            print('Número de cuenta inválido.')


def crear_cuenta(cuentas):
    nombre_cuenta = input('Ingrese el nombre de la nueva cuenta: ')
    cuenta = Cuenta(nombre_cuenta)
    cuentas.append(cuenta)
    print(f'Cuenta {nombre_cuenta} creada correctamente.')
    with open(f'{nombre_cuenta}.csv', 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(['Fecha', 'hora', 'Descripcion', 'Monto'])


def menu_principal():
    """
    Esta función prenseta el menú principal y ejecuta las acciones sobre la cuenta

    Returns:
        None
    """

    cuentas = listar_cuentas()

    while True:
        print('\nMenú principal:')
        print('1. Listar cuentas')
        print('2. Operaciones en cuenta')
        print('3. Crear nueva cuenta')
        print('4. Salir')

        opcion = int(input('Ingrese una opcion: '))

        if opcion == 1:
            imprimir_cuentas(cuentas)
        elif opcion == 2:
            seleccionar_cuenta(cuentas)
        elif opcion == 3:
            crear_cuenta(cuentas)
        elif opcion == 4:
            print('Saliendo del programa...')
            break
        else:
            print('Opción inválida. Intente de nuevo...')


if __name__ == '__main__':
    menu_principal()
