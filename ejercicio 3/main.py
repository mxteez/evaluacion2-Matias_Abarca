from clases.cuentas import CuentaCorriente, CuentaAhorro
from clases.banco import Banco

def main():
    print("=== SISTEMA BANCARIO INICIADO ===")
    
    # 1. Instanciar el Banco
    mi_banco = Banco("Banco Central Python")

    # 2. Creación de cuentas (2 Corrientes, 2 Ahorro)
    cc1 = CuentaCorriente(numero="C001", titular="Juan Pérez", saldo_inicial=100000, linea_credito=50000)
    cc2 = CuentaCorriente(numero="C002", titular="Ana Gómez", saldo_inicial=0, linea_credito=20000)
    
    ca1 = CuentaAhorro(numero="A001", titular="Carlos Ruiz", saldo_inicial=50000, tasa_interes=0.05) # 5% interés
    ca2 = CuentaAhorro(numero="A002", titular="Lucía Diaz", saldo_inicial=200000)

    # 3. Agregar cuentas al banco
    mi_banco.agregar_cuenta(cc1)
    mi_banco.agregar_cuenta(cc2)
    mi_banco.agregar_cuenta(ca1)
    mi_banco.agregar_cuenta(ca2)

    print("\n--- SIMULACIÓN DE MOVIMIENTOS ---")

    # 4. Ejecución de depósitos y retiros
    
    # Cuenta Corriente 1: Retiro normal
    cc1.retirar(50000) 
    
    # Cuenta Corriente 2: Sobregiro (usa línea de crédito)
    # Tiene 0, retira 10.000. Queda en -10.000 (permitido porque línea es 20.000)
    print("Intentando sobregiro en C002:")
    cc2.retirar(10000) 

    # Cuenta Ahorro 1: Depósito y Retiro
    ca1.depositar(20000)
    ca1.retirar(100000) # Debería fallar, saldo insuficiente (70k) y no tiene línea crédito

    # 5. Aplicar intereses a una cuenta de ahorro
    print("\n--- APLICANDO INTERESES ---")
    ca1.aplicar_interes() # Saldo era 70.000, interés 5% = 3.500. Nuevo saldo = 73.500

    # 6. Impresión de reportes
    
    # Reporte individual y su historial
    mi_banco.mostrar_info_cuenta("C002")
    mi_banco.mostrar_historial_cuenta("C002")

    mi_banco.mostrar_info_cuenta("A001")
    mi_banco.mostrar_historial_cuenta("A001")

    # 7. Saldo total administrado
    total_banco = mi_banco.obtener_saldo_total_banco()
    print(f"\n========================================")
    print(f"SALDO TOTAL ADMINISTRADO POR EL BANCO: ${total_banco}")
    print(f"========================================")

if __name__ == "__main__":
    main()