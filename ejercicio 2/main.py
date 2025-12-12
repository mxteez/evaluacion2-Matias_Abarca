from clases.trabajadores import Vendedor, Gerente, Practicante
from clases.empresa import Empresa

def main():
    # 1. Creamos la empresa
    mi_empresa = Empresa("Tech Solutions Ltda.")

    # 2. Creamos trabajadores con distintos roles
    
    # Gerente: Sueldo base 2.5M + Bono de 500k
    g1 = Gerente("Ana Pérez", "12.345.678-9", sueldo_base=2500000, bono_gestion=500000)
    
    # Vendedor: Sueldo base 500k + 10% de comisión sobre ventas de 5M
    v1 = Vendedor("Carlos Díaz", "15.555.444-K", sueldo_base=500000, comision_pct=0.10, ventas_mes=5000000)
    
    # Vendedor 2: Mismas condiciones, pero vendió menos
    v2 = Vendedor("Lucía Gómez", "18.999.000-1", sueldo_base=500000, comision_pct=0.10, ventas_mes=2000000)

    # Practicante: 160 horas al mes a 5.000 la hora
    p1 = Practicante("Pedro Ruiz", "20.123.123-4", valor_hora=5000, horas_trabajadas=160)

    # Trabajador inactivo (ejemplo: licencia médica larga o desvinculado pero en registro)
    v_inactivo = Vendedor("Mario Bross", "10.000.000-1", sueldo_base=600000, comision_pct=0.05, ventas_mes=0)
    v_inactivo.activo = False

    # 3. Incorporar trabajadores a la empresa
    mi_empresa.agregar_trabajador(g1)
    mi_empresa.agregar_trabajador(v1)
    mi_empresa.agregar_trabajador(v2)
    mi_empresa.agregar_trabajador(p1)
    mi_empresa.agregar_trabajador(v_inactivo)

    # 4. Probar funcionalidades
    
    # Listar todos (para ver el resumen legible solicitado en el punto 4)
    mi_empresa.listar_trabajadores()

    # Listar solo activos
    mi_empresa.listar_activos()

    # Calcular indicadores globales (Gasto total)
    mi_empresa.calcular_gasto_mensual()

if __name__ == "__main__":
    main()