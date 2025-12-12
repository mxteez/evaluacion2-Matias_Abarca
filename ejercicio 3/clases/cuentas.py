class CuentaBancaria:
    def __init__(self, numero, titular, saldo_inicial=0):
        self.numero = numero
        self.titular = titular
        self._saldo = saldo_inicial
        self.movimientos = []  # Lista para el historial
        self.tipo = "Genérica"
        # Registro del saldo inicial
        if saldo_inicial > 0:
            self.registrar_movimiento(f"SALDO INICIAL {saldo_inicial}")

    def registrar_movimiento(self, descripcion):
        """Agrega un texto al historial de movimientos."""
        self.movimientos.append(descripcion)

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            self.registrar_movimiento(f"DEPÓSITO {monto}")
            print(f"Depósito de {monto} realizado en cuenta {self.numero}.")
        else:
            print("El monto a depositar debe ser positivo.")

    def retirar(self, monto):
        # Este método será sobrescrito o extendido por las clases hijas
        if monto > 0 and self._saldo >= monto:
            self._saldo -= monto
            self.registrar_movimiento(f"RETIRO {monto}")
            print(f"Retiro de {monto} realizado en cuenta {self.numero}.")
            return True
        else:
            print(f"Fondos insuficientes o monto inválido en cuenta {self.numero}.")
            return False

    def obtener_saldo(self):
        return self._saldo

    def obtener_historial(self):
        return self.movimientos

    def __str__(self):
        return f"[{self.tipo}] N°: {self.numero} | Titular: {self.titular} | Saldo: ${self._saldo}"


class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero, titular, saldo_inicial=0, linea_credito=50000):
        super().__init__(numero, titular, saldo_inicial)
        self.linea_credito = linea_credito
        self.tipo = "Cuenta Corriente"

    def retirar(self, monto):
        """
        Permite retirar si el saldo + línea de crédito cubre el monto.
        El saldo puede quedar negativo hasta el límite de la línea de crédito.
        """
        saldo_disponible = self._saldo + self.linea_credito
        
        if monto > 0 and saldo_disponible >= monto:
            self._saldo -= monto
            self.registrar_movimiento(f"RETIRO {monto}")
            print(f"Retiro de {monto} realizado (CC con línea de crédito).")
            return True
        else:
            print(f"Fondos insuficientes (excede línea de crédito) en cuenta {self.numero}.")
            return False


class CuentaAhorro(CuentaBancaria):
    def __init__(self, numero, titular, saldo_inicial=0, tasa_interes=0.02):
        super().__init__(numero, titular, saldo_inicial)
        self.tasa_interes = tasa_interes  # Ejemplo: 0.02 es 2%
        self.tipo = "Cuenta Ahorro"

    def aplicar_interes(self):
        """Calcula el interés basado en el saldo actual y lo suma."""
        if self._saldo > 0:
            interes_ganado = int(self._saldo * self.tasa_interes)
            self._saldo += interes_ganado
            self.registrar_movimiento(f"INTERÉS {interes_ganado}")
            print(f"Interés de {interes_ganado} aplicado a la cuenta {self.numero}.")