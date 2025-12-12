from .vehiculos import Vehiculo

class Flota:
    def __init__(self):
        self.lista_vehiculos = []

    def buscar_vehiculo(self, patente):
        """Retorna el objeto vehículo si existe, o None si no."""
        for v in self.lista_vehiculos:
            if v.patente == patente:
                return v
        return None

    def agregar_vehiculo(self, vehiculo: Vehiculo):
        if self.buscar_vehiculo(vehiculo.patente):
            print(f"Error: El vehículo con patente {vehiculo.patente} ya existe.")
            return False
        
        self.lista_vehiculos.append(vehiculo)
        print(f"Vehículo {vehiculo.patente} agregado exitosamente.")
        return True

    def eliminar_vehiculo(self, patente):
        vehiculo = self.buscar_vehiculo(patente)
        if vehiculo:
            self.lista_vehiculos.remove(vehiculo)
            print(f"Vehículo {patente} eliminado.")
        else:
            print(f"Error: No se encontró el vehículo {patente} para eliminar.")

    def mostrar_detalle_flota(self):
        print("\n--- DETALLE DE LA FLOTA ---")
        if not self.lista_vehiculos:
            print("La flota está vacía.")
        for v in self.lista_vehiculos:
            print(v)
        print("---------------------------")

    def calcular_consumo_total(self, km):
        total_litros = 0
        print(f"\n--- CALCULO DE CONSUMO PARA TRAYECTO DE {km} KM ---")
        
        for v in self.lista_vehiculos:
            consumo_individual = v.calcular_consumo(km)
            total_litros += consumo_individual
            print(f" - {v.patente}: {consumo_individual} litros estimados.")
            
        print(f"TOTAL FLOTA: {round(total_litros, 2)} litros de combustible necesarios.")
        return total_litros