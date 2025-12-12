class Vehiculo:
    def __init__(self, patente, marca, modelo, año):
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def calcular_consumo(self, km):
        pass

    def __str__(self):
        return f"[{self.patente}] {self.marca} {self.modelo} ({self.año})"


class Automovil(Vehiculo):
    def __init__(self, patente, marca, modelo, año, puertas):
        super().__init__(patente, marca, modelo, año)
        self.puertas = puertas

    def calcular_consumo(self, km):
        # Lógica: Un auto promedio rinde 12 km/litro aprox.
        rendimiento = 12 
        litros = km / rendimiento
        return round(litros, 2)

    def __str__(self):
        base = super().__str__()
        return f"{base} - Tipo: Automóvil ({self.puertas} puertas)"


class Motocicleta(Vehiculo):
    def __init__(self, patente, marca, modelo, año, cilindrada):
        super().__init__(patente, marca, modelo, año)
        self.cilindrada = cilindrada

    def calcular_consumo(self, km):
        # Lógica: Las motos rinden más. Supongamos 25 km/litro, 
        # pero si tiene mucha cilindrada gasta un poco más.
        rendimiento = 25 - (self.cilindrada / 1000)
        litros = km / rendimiento
        return round(litros, 2)

    def __str__(self):
        base = super().__str__()
        return f"{base} - Tipo: Motocicleta ({self.cilindrada}cc)"


class Camion(Vehiculo):
    def __init__(self, patente, marca, modelo, año, carga_max_kg):
        super().__init__(patente, marca, modelo, año)
        self.carga_max_kg = carga_max_kg

    def calcular_consumo(self, km):
        # Lógica: El camión gasta mucho más.
        # Supongamos un rendimiento base de 5 km/litro.
        # A mayor capacidad de carga, menor rendimiento.
        rendimiento = 5 - (self.carga_max_kg / 10000) 
        # Evitar división por cero o negativos si la carga es enorme
        if rendimiento < 1: rendimiento = 1
        
        litros = km / rendimiento
        return round(litros, 2)

    def __str__(self):
        base = super().__str__()
        return f"{base} - Tipo: Camión (Carga: {self.carga_max_kg}kg)"