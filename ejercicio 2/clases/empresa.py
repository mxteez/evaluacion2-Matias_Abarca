class Empresa:
    def __init__(self, nombre_empresa):
        self.nombre_empresa = nombre_empresa
        self.trabajadores = []

    def agregar_trabajador(self, trabajador):
        self.trabajadores.append(trabajador)

    def listar_trabajadores(self):
        print(f"\n--- Nómina de Trabajadores: {self.nombre_empresa} ---")
        for t in self.trabajadores:
            print(t)

    def listar_activos(self):
        print(f"\n--- Trabajadores Activos ---")
        activos = [t for t in self.trabajadores if t.activo]
        for t in activos:
            print(t)

    def calcular_gasto_mensual(self):
        total = 0
        print(f"\n--- Cálculo de Gasto Mensual (Solo Activos) ---")
        for t in self.trabajadores:
            if t.activo:
                remuneracion = t.calcular_remuneracion()
                total += remuneracion
                # Opcional: Mostrar detalle del cálculo
                print(f"+ {t.nombre}: ${remuneracion:,}")
        
        print(f"===================================")
        print(f"GASTO TOTAL MENSUAL: ${total:,}")
        return total