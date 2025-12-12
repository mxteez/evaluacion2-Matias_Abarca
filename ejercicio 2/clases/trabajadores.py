class Trabajador:
    def __init__(self, nombre, rut, sueldo_base, activo=True):
        self.nombre = nombre
        self.rut = rut
        self.sueldo_base = sueldo_base
        self.activo = activo
        self.tipo = "Genérico"

    def calcular_remuneracion(self):
        """Método base, se sobrescribe en las clases hijas"""
        return self.sueldo_base

    def __str__(self):
        # Usamos f-strings para formatear el dinero con separador de miles
        sueldo_final = self.calcular_remuneracion()
        estado = "Activo" if self.activo else "Inactivo"
        return (f"[{self.tipo}] {self.nombre} (RUT: {self.rut}) | "
                f"Estado: {estado} | "
                f"Base: ${self.sueldo_base:,} | "
                f"Final: ${sueldo_final:,}")


class Vendedor(Trabajador):
    def __init__(self, nombre, rut, sueldo_base, comision_pct, ventas_mes):
        super().__init__(nombre, rut, sueldo_base)
        self.tipo = "Vendedor"
        self.comision_pct = comision_pct  # Ejemplo: 0.10 para 10%
        self.ventas_mes = ventas_mes

    def calcular_remuneracion(self):
        # Sueldo base + (Ventas * % Comisión)
        comision = self.ventas_mes * self.comision_pct
        return int(self.sueldo_base + comision)


class Gerente(Trabajador):
    def __init__(self, nombre, rut, sueldo_base, bono_gestion):
        super().__init__(nombre, rut, sueldo_base)
        self.tipo = "Gerente"
        self.bono_gestion = bono_gestion

    def calcular_remuneracion(self):
        # Sueldo base + Bono
        return int(self.sueldo_base + self.bono_gestion)


class Practicante(Trabajador):
    def __init__(self, nombre, rut, valor_hora, horas_trabajadas):
        # El practicante no tiene "sueldo base" fijo mensual, pasamos 0 al padre
        # y su lógica se basa puramente en horas.
        super().__init__(nombre, rut, sueldo_base=0)
        self.tipo = "Practicante"
        self.valor_hora = valor_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_remuneracion(self):
        # Horas * Valor hora
        return int(self.horas_trabajadas * self.valor_hora)