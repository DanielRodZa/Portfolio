import csv
import datetime


def registrar_movimiento(cuenta, fecha, descripcion, monto):
    """
    Esta función registra un nuevo movimiento (ingreso o gasto) en el cuenta
    Args:
        cuenta (string): Nombre de la cuenta
        fecha (string): Fecha del movimiento (formato dd/mm/yyyy)
        descripcin (string): Descripcion del movimiento o motivo
        monto (float): Monto del movimiento

    Ejemplo de uso:
    registrar_movimiento('BBVA','01/01/2020','Compra supermecado', -120.50)

    Returns:
        None
    """
    movimiento = [cuenta, fecha, descripcion, monto]
    with open('registro.csv', 'a', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(movimiento)


def consultar_saldo(cuenta):
    """
    Esta función consulta el saldo actual de una cuenta especifica.

    Args:
        cuenta (string): Nombre de la cuenta (BBVA, Citibanamex, Debito Nu)

    Returns:
        float: Saldo actual de la cuenta.

    Ejemplo de uso:
    saldo_banco = consultar_saldo('BBVA')
    print(f'Saldo BBVA: {saldo_banco}')
    """

    saldo = 0.0
    with open('registro.csv', 'r') as archivo:
        lector = csv.reader(archivo)
        for movimiento in lector:
            if movimiento[0] == cuenta:
                saldo += float(movimiento[3])

    return saldo

def generar_estado_de_cuenta(cuenta, fecha_inicio, fecha_fin):
    """
    Esta funcion genera un estado de cuenta detallado por fechas para una cuenta específica.
    Args:
        cuenta (string): Nombre de la cuenta
        fecha_inicio (string): Fecha inicial al estado de cuenta
        fecha_fin (string): Fecha final al estado de cuenta

    Ejemplo de uso:
    generar_estado_de_cuenta('BBVA','01/01/2024','01/02/2024')

    Returns:
        None
    """
    print(f'Generando estado de cuenta - {cuenta}')
    print(f'FECHA INICIO: {fecha_inicio} - FECHA FIN: {fecha_fin}')

    saldo_inicial = consultar_saldo(cuenta)
    print(f'SALDO INICIAL: {saldo_inicial}')

    movimientos = []
    with open('registros.csv','r') as archivo:
        lector = csv.reader(archivo)
        for movimiento in lector:
            movimientos.append(movimiento)

    for movimiento in movimientos:
        fecha, descripcion, monto = movimiento[1:]
        print(f'{fecha} - {descripcion}: {monto}')

    saldo_final = saldo_inicial + sum(float(movimiento[3]) for movimiento in movimientos)
    print(f'SALDO FINAL: {saldo_final}')

def menu_principal():
    """
    Esta función presenta el menu principal y ejecuta las acciones de las opciones

    Returns:
        None
    """
    while True:
        print('\nMenú principal:')
        print('1 - Registar movimiento')
        print('2 - Consultar saldo')
        print('3 - Genera estado de cuenta')
        print('4 - Salir')

        opcion = int(input('Ingrese una opción:\n'))

        if opcion == 1:
            cuenta = input('Ingrese la cuenta (Ejemplo: BBVA dédito, BBVA crédito, Nu Crédito)\n')
            fecha = input('Ingrese la fecha del movimiento (dd/mm/aaaa)\n')
            descripcion = input('Ingrese el motivo o descripción del movimiento\n')
            monto = float(input('Ingrese el monto del movimiento\n'))
            registrar_movimiento(cuenta, fecha, descripcion, monto)
            print('El movimiento registrado correctamente:')
            print(f'{cuenta} - {fecha}: {monto} para {descripcion}')
        elif opcion == 2:
            cuenta = input('Ingrese la cuenta que desea consultar (Ejemplo: BBVA dédito, BBVA crédito, Nu Crédito):\n')
            saldo = consultar_saldo(cuenta)
            print(f'El saldo actual de la {cuenta} es: {saldo}')
        elif opcion == 3:
            cuenta = input('Ingrese la cuenta que desea consultar (Ejemplo: BBVA dédito, BBVA crédito, Nu Crédito):\n')
            fecha_inicio = input('Ingrese la fecha inicial:\n')
            fecha_fin = input('Ingrese la fecha final:\n')
            generar_estado_de_cuenta(cuenta, fecha_inicio, fecha_fin)
        elif opcion == 4:
            print('Finalizando programa...')
            break
        else:
            print('Opción no válida, intenta de nuevo...')

if __name__ == '__main__':
    menu_principal()