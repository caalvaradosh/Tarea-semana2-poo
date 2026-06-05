# Programa: Cuenta Bancaria
# Autor: Clide
# Asignatura: Programación Orientada a Objetos

class CuentaBancaria:
    def __init__(self, titular, numero_cuenta, saldo):
        # Atributos
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    # Método para depositar dinero
    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se depositaron ${cantidad:.2f}.")
        print(f"Nuevo saldo: ${self.saldo:.2f}")

    # Método para retirar dinero
    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se retiraron ${cantidad:.2f}.")
            print(f"Nuevo saldo: ${self.saldo:.2f}")
        else:
            print("Fondos insuficientes.")

    # Método para mostrar información de la cuenta
    def mostrar_datos(self):
        print("Titular:", self.titular)
        print("Número de cuenta:", self.numero_cuenta)
        print("Saldo:", f"${self.saldo:.2f}")


# ==========================
# Creación de objetos
# ==========================

cuenta1 = CuentaBancaria("Clide López", "00123456", 500.00)
cuenta2 = CuentaBancaria("Ana Torres", "00987654", 1000.00)

# ==========================
# Uso del objeto cuenta1
# ==========================

print("=== CUENTA 1 ===")
cuenta1.mostrar_datos()
cuenta1.depositar(150)
cuenta1.retirar(200)

# ==========================
# Uso del objeto cuenta2
# ==========================

print("\n=== CUENTA 2 ===")
cuenta2.mostrar_datos()
cuenta2.depositar(300)
cuenta2.retirar(500)