class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = [] # Lista para almacenar objetos de tipo cuenta

    def agregar_cuenta(self, cuenta):
        # Verificamos si ya existe
        if self.buscar_cuenta(cuenta.numero):
            print(f"Error: La cuenta {cuenta.numero} ya existe.")
        else:
            self.cuentas.append(cuenta)
            print(f"Cuenta {cuenta.numero} agregada al sistema.")

    def buscar_cuenta(self, numero):
        """Busca una cuenta por número y retorna el objeto o None."""
        for cuenta in self.cuentas:
            if cuenta.numero == numero:
                return cuenta
        return None

    def mostrar_info_cuenta(self, numero):
        cuenta = self.buscar_cuenta(numero)
        if cuenta:
            print("\n--- Información de la Cuenta ---")
            print(cuenta) # Usa el __str__ de la clase
        else:
            print("Cuenta no encontrada.")

    def mostrar_historial_cuenta(self, numero):
        cuenta = self.buscar_cuenta(numero)
        if cuenta:
            print(f"\n--- Historial Cuenta {numero} ({cuenta.titular}) ---")
            for mov in cuenta.obtener_historial():
                print(f" - {mov}")
        else:
            print("Cuenta no encontrada.")

    def obtener_saldo_total_banco(self):
        """Suma el saldo de todas las cuentas registradas."""
        total = sum(cuenta.obtener_saldo() for cuenta in self.cuentas)
        return total