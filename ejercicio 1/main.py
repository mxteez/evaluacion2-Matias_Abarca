from clases.vehiculos import Automovil, Motocicleta, Camion
from clases.flota import Flota

def main():
    # 1. Instanciamos el sistema gestor
    mi_flota = Flota()

    # 2. Creamos varios vehículos de distintos tipos
    auto1 = Automovil("AB-1234", "Toyota", "Corolla", 2020, 4)
    auto2 = Automovil("CD-5678", "Suzuki", "Swift", 2018, 5)
    
    moto1 = Motocicleta("MT-99", "Honda", "CB500", 2022, 500)
    
    camion1 = Camion("TR-5000", "Volvo", "FH16", 2019, 20000) # 20 mil kg carga

    print("--- INICIO DE SIMULACIÓN ---\n")

    # 3. Agregarlos a la flota
    mi_flota.agregar_vehiculo(auto1)
    mi_flota.agregar_vehiculo(moto1)
    mi_flota.agregar_vehiculo(camion1)
    mi_flota.agregar_vehiculo(auto2)
    
    # Intento de agregar duplicado para probar validación
    mi_flota.agregar_vehiculo(auto1) 

    # 4. Mostrar información de cada vehículo
    mi_flota.mostrar_detalle_flota()

    # 5. Calcular consumo para un trayecto común (ej. 150 km)
    # Esto demuestra el polimorfismo: cada vehículo calcula distinto.
    mi_flota.calcular_consumo_total(150)

    # 6. Prueba de eliminación y búsqueda
    print("\n--- PRUEBA DE BÚSQUEDA Y ELIMINACIÓN ---")
    buscado = mi_flota.buscar_vehiculo("MT-99")
    if buscado:
        print(f"Vehículo encontrado: {buscado}")
    
    mi_flota.eliminar_vehiculo("MT-99")
    mi_flota.mostrar_detalle_flota()

if __name__ == "__main__":
    main()