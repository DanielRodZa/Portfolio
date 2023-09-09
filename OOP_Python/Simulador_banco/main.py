
class Cliente:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"Cliente: {self.nombre}, Direccion: {self.direccion}, Teléfono {self.telefono}"

class CuentaBancaria:
    def __init__(self, cliente, saldo_inicial=0):
        self.cliente = cliente
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return f"Depósito de ${cantidad} realizado. Saldo actual: ${self.saldo}."
        else:
            return "La cantidad de depósito deve ser mayor que cero."

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            return f"Retiro de ${cantidad} ralizado. Saldo actual: ${self.saldo}."
        elif cantidad > self.saldo:
            return "Saldo insuficiente para realizar el retiro."
        else:
            return "La cantidad de retiro debe ser mayor que cero."

    def obtener_saldo(self):
        return f"Saldo actual de la cuenta de {self.cliente.nombre}: ${self.saldo}."

    def __str__(self):
        return f"CUneta de {self.cliente.nombre}, Saldo: ${self.saldo}."

class Transaccion:
    @staticmethod
    def transferir(origen, destino, cantidad):
        if cantidad > 0 and cantidad <= origen.saldo:
            origen.retirar(cantidad)
            destino.depositar(cantidad)
            return f"Transferencia exitosa de ${cantidad} de {origen.cliente.nombre} a {destino.cliente.nombre}."
        elif cantidad > origen.saldo:
            return "Saldo insuficiente para realizar la transferencia."
        else:
            return "La cantidad que deseas transferir debe ser mayor a 0"

def main():
    cliente1 = Cliente("Daniel Rodriguez","Calle principal #12", "555-555-6565")
    cliente2 = Cliente("Juan Pérez", "Calle avenida #45", "555-555-1234")

    cuenta1 = CuentaBancaria(cliente1, 1000)
    cuenta2 = CuentaBancaria(cliente2, 500)

    print(Transaccion.transferir(cuenta1, cuenta2, 200))
    print(cuenta1)
    print(cuenta2)

if __name__ == "__main__":
    main()