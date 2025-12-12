# Importamos las clases desde la estructura de carpetas
from clases.producto import ProductoFisico, ProductoDigital
from clases.carrito import Carrito

def main():
    print("=== SISTEMA DE VENTAS ONLINE ===")

    # 1. Crear Productos (Simulación de Base de Datos)
    # Físicos
    libro = ProductoFisico("F01", "Libro Python", 15000, 10, peso="0.5kg", categoria_envio="liviano")
    laptop = ProductoFisico("F02", "Laptop Gamer", 800000, 5, peso="2.5kg", categoria_envio="pesado")
    
    # Digitales
    curso = ProductoDigital("D01", "Curso Django", 20000, 100, tamano_archivo="5GB", tipo_licencia="personal")
    software = ProductoDigital("D02", "Licencia ERP", 50000, 50, tamano_archivo="200MB", tipo_licencia="comercial")

    # Mostrar stock inicial
    print("\n--- Stock Inicial ---")
    print(libro)
    print(laptop)
    print(software)

    # 2. Inicializar Carrito
    mi_carrito = Carrito()

    # 3. Agregar productos
    print("\n--- Agregando productos al carrito ---")
    mi_carrito.agregar_producto(libro, 2)       # Físico, envío liviano
    mi_carrito.agregar_producto(laptop, 1)      # Físico, envío pesado
    mi_carrito.agregar_producto(software, 1)    # Digital, licencia comercial (+20%)
    
    # 4. Intentar agregar más del stock disponible (Prueba de validación)
    mi_carrito.agregar_producto(laptop, 10)     # Debería fallar

    # 5. Mostrar detalle
    mi_carrito.mostrar_detalle()

    # 6. Calcular Total
    total_pagar = mi_carrito.obtener_total_general()
    print(f"\n TOTAL A PAGAR: ${total_pagar:.0f}")

    # 7. Eliminar un producto y recalcular
    print("\n--- Eliminando Laptop del carrito ---")
    mi_carrito.eliminar_producto("F02")
    
    mi_carrito.mostrar_detalle()
    print(f" NUEVO TOTAL: ${mi_carrito.obtener_total_general():.0f}")

    # 8. Verificar que el stock se redujo en los objetos originales
    print("\n--- Verificación de Stock (post-venta) ---")
    print(libro) # Debería tener 8 (eran 10, se compraron 2)

if __name__ == "__main__":
    main()